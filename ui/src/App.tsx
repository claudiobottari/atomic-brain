import { useState, useEffect } from 'react'
import { Search, Brain, Folder, BarChart2, ArrowLeft, Database } from 'lucide-react'
import './App.css'

interface Concept {
  id: string;
  title: string;
  content: string;
  source: string;
  timestamp: string;
  tags: string;
}

interface Stats {
  total_concepts: number;
  categories: Record<string, number>;
}

function App() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<Concept[]>([])
  const [stats, setStats] = useState<Stats | null>(null)
  const [selectedConcept, setSelectedConcept] = useState<Concept | null>(null)
  const [loading, setLoading] = useState(false)

  const API_BASE = "http://localhost:8000/api"

  useEffect(() => {
    fetchStats()
  }, [])

  const fetchStats = async () => {
    try {
      const res = await fetch(`${API_BASE}/stats`)
      const data = await res.json()
      setStats(data)
    } catch (e) {
      console.error("Failed to fetch stats", e)
    }
  }

  const handleSearch = async (e?: React.FormEvent) => {
    if (e) e.preventDefault()
    if (!query) return

    setLoading(true)
    try {
      const res = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`)
      const data = await res.json()
      setResults(data.results)
      setSelectedConcept(null)
    } catch (e) {
      console.error("Search failed", e)
    } finally {
      setLoading(false)
    }
  }

  const viewConcept = async (id: string) => {
    try {
      const res = await fetch(`${API_BASE}/concepts/${id}`)
      const data = await res.json()
      setSelectedConcept(data)
    } catch (e) {
      console.error("Failed to fetch concept", e)
    }
  }

  return (
    <div className="app-container">
      <aside className="sidebar">
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '30px' }}>
          <Brain color="var(--accent)" size={32} />
          <h2 style={{ margin: 0, fontSize: '20px' }}>AtomicBrain</h2>
        </div>

        <nav style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--text-muted)', cursor: 'pointer' }} onClick={() => {setSelectedConcept(null); setResults([])}}>
            <Search size={18} />
            <span>Search</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--text-muted)' }}>
            <Folder size={18} />
            <span>Categories</span>
          </div>
        </nav>

        <div className="stats-panel">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '15px' }}>
            <BarChart2 size={18} />
            <span style={{ fontWeight: '600' }}>Vault Stats</span>
          </div>
          <div className="stat-item">
            <span>Total Concepts</span>
            <span>{stats?.total_concepts || 0}</span>
          </div>
          <div style={{ marginTop: '10px' }}>
            {stats && Object.entries(stats.categories).map(([name, count]) => (
              <div key={name} className="stat-item" style={{ fontSize: '12px' }}>
                <span>{name}</span>
                <span>{count}</span>
              </div>
            ))}
          </div>
          
          <div style={{ marginTop: '30px', display: 'flex', alignItems: 'center', gap: '10px', fontSize: '12px' }}>
             <Database size={14} color="#27ae60" />
             <span style={{color: '#27ae60'}}>Index Live</span>
          </div>
        </div>
      </aside>

      <main className="main-content">
        {!selectedConcept ? (
          <>
            <header>
              <div className="status-badge">System Online v1.0.0</div>
              <h1>Ground your AI in local knowledge.</h1>
              <p style={{ color: 'var(--text-muted)', marginBottom: '40px' }}>
                Search across your Obsidian vault with semantic understanding.
              </p>
            </header>

            <form className="search-bar" onSubmit={handleSearch}>
              <input 
                type="text" 
                placeholder="Ask your brain anything..." 
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              />
              <button type="submit" disabled={loading}>
                {loading ? "Searching..." : "Search"}
              </button>
            </form>

            <div className="results-grid">
              {results.map((res) => (
                <div key={res.id} className="concept-card" onClick={() => viewConcept(res.id)}>
                  <h3>{res.title}</h3>
                  <p className="snippet">{res.content.substring(0, 120)}...</p>
                  <div style={{ fontSize: '11px', color: 'var(--accent)', marginTop: '10px' }}>
                    {res.tags}
                  </div>
                </div>
              ))}
              {results.length === 0 && query && !loading && (
                <p style={{ color: 'var(--text-muted)' }}>No results found for "{query}"</p>
              )}
            </div>
          </>
        ) : (
          <div className="concept-detail">
            <div className="back-button" onClick={() => setSelectedConcept(null)}>
              <ArrowLeft size={18} />
              Back to search
            </div>
            <h1>{selectedConcept.title}</h1>
            <div className="metadata">
              <div>ID: {selectedConcept.id}</div>
              <div>Source: {selectedConcept.source}</div>
              <div>Ingested: {new Date(selectedConcept.timestamp).toLocaleString()}</div>
              <div>Tags: {selectedConcept.tags}</div>
            </div>
            <div className="content-body">
              {selectedConcept.content.split('\n').map((line: string, i: number) => (
                <p key={i}>{line}</p>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default App

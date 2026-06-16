flowchart TD
  %% Game Glitch Investigator - architecture overview
  U[Player / Browser]
  App[Streamlit app<br/>`app.py`]
  Sidebar[Sidebar UI]
  Main[Main UI]
  Dev[Developer Debug Info]
  Logic[Logic Layer<br/>`logic_utils.py`]
  Parse[parse_guess()]
  Range[get_range_for_difficulty()]
  Score[update_score()]
  Session[Streamlit session state<br/>`st.session_state`]
  Tests[Unit tests<br/>`tests/`]
  Req[requirements.txt]

  U -->|open app / submit guess| App
  App --> Sidebar
  App --> Main
  App --> Dev

  Main -->|submit guess| Logic
  Logic --> Parse
  Logic --> Range
  Logic --> Score

  Parse -->|validated guess| Score
  Range -->|difficulty params| Logic
  Score -->|update| Session
  Logic -->|persist| Session
  Session -->|read/write| App

  Tests -->|unit tests| Logic
  Req -->|env| App

  classDef grey fill:#f5f5f5,stroke:#ddd
  class App,Sidebar,Main,Dev,Logic,Parse,Range,Score,Session,Tests,Req grey

  %% explanatory note
  subgraph Notes[ ]
    N1[Session stores: secret_number, attempts_left, history, score]
  end
  N1 --- Session

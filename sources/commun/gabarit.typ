// Gabarit commun des livrables du corpus (Typst 0.15.1).
// Format lettre, texte justifié avec césure française, tableaux en sans empattement.

#let encre = rgb("#1b2430")
#let accent = rgb("#1f4e79")
#let accent-pale = rgb("#e8eef5")
#let filet = rgb("#c5ced9")
#let zebre = rgb("#f5f7fa")
#let gris = rgb("#5b6573")
#let serif = ("Libertinus Serif",)
#let sans = ("Segoe UI",)

#let note(titre-court: "", pied: [], body) = {
  set page(
    paper: "us-letter",
    margin: (left: 72pt, right: 72pt, top: 78pt, bottom: 72pt),
    header: context {
      let p = here().page()
      if p <= 1 { return }
      let hs = query(heading.where(level: 2))
      let ici = hs.filter(h => h.location().page() == p)
      let avant = hs.filter(h => h.location().page() < p)
      let courant = if ici.len() > 0 { ici.first().body } else if avant.len() > 0 { avant.last().body }
      set text(font: sans, size: 7.5pt, fill: gris)
      grid(columns: (auto, 1fr), column-gutter: 12pt,
        text(weight: "semibold", fill: accent, titre-court),
        align(right, if courant != none { courant }))
      v(-4pt)
      line(length: 100%, stroke: 0.5pt + filet)
    },
    footer: context {
      if here().page() <= 1 { return }
      set text(font: sans, size: 7.5pt, fill: gris)
      grid(columns: (1fr, 1fr),
        pied,
        align(right)[Page #counter(page).display() sur #counter(page).final().first()])
    },
  )
  set document(author: "André-Guy Bruneau")
  set text(font: serif, size: 10.8pt, lang: "fr", region: "CA", hyphenate: true, fill: encre)
  set par(justify: true, leading: 0.62em, spacing: 0.95em, linebreaks: "optimized")
  set list(indent: 0.4em, body-indent: 0.55em, spacing: 0.75em,
    marker: text(fill: accent, size: 0.8em, baseline: -0.1em, sym.bullet))
  set enum(indent: 0.4em, body-indent: 0.55em, spacing: 0.75em)
  show link: set text(fill: accent)
  show strong: set text(weight: "bold")

  // Parties (niveau 1) : page neuve, bandeau.
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(70pt)
    block(width: 100%, below: 36pt, {
      line(length: 42pt, stroke: 2.5pt + accent)
      v(10pt)
      set text(font: sans, size: 22pt, weight: "semibold", fill: accent)
      set par(justify: false, leading: 0.4em)
      it.body
    })
  }
  // Chapitres et annexes (niveau 2).
  show heading.where(level: 2): it => block(above: 26pt, below: 12pt, sticky: true, {
    set text(font: sans, size: 14pt, weight: "semibold", fill: accent)
    set par(justify: false, leading: 0.45em)
    it.body
    v(-6pt)
    line(length: 100%, stroke: 0.6pt + filet)
  })
  show heading.where(level: 3): it => block(above: 18pt, below: 8pt, sticky: true, {
    set text(font: sans, size: 11pt, weight: "semibold", fill: encre)
    set par(justify: false)
    it.body
  })
  show heading.where(level: 4): it => block(above: 12pt, below: 6pt, sticky: true,
    text(font: sans, size: 10pt, weight: "semibold", style: "italic", it.body))

  // Tableaux : en-tête répété, zébrure, texte aligné à gauche (pas de justification
  // dans les cellules étroites).
  show figure.where(kind: table): set block(breakable: true)
  show figure.where(kind: table): set align(left)
  show figure.where(kind: table): set figure(gap: 6pt)
  show figure.where(kind: table): set block(above: 14pt, below: 16pt)
  set table(
    stroke: none,
    inset: (x: 5pt, y: 4.2pt),
    fill: (_, y) => if y == 0 { accent } else if calc.even(y) { zebre },
  )
  set table.hline(stroke: 0.6pt + accent)
  show table: set text(font: sans, size: 8pt)
  show table: set par(justify: false, leading: 0.5em, spacing: 0.6em)
  show table: set list(indent: 0pt, body-indent: 0.4em, spacing: 0.4em)
  show table.cell.where(y: 0): set text(fill: white, weight: "semibold")
  show table: it => block(stroke: (bottom: 0.6pt + filet), it)

  set figure.caption(separator: [ — ])
  show figure.caption: set text(font: sans, size: 8pt, fill: gris)
  body
}

// Fiche signalétique de la couverture : paires rubrique / valeur.
#let fiche(..cellules) = {
  let c = cellules.pos()
  set text(font: sans, size: 8.3pt)
  set par(justify: false, leading: 0.5em)
  block(width: 100%, stroke: (top: 1.2pt + accent, bottom: 0.6pt + filet), inset: (y: 4pt),
    grid(columns: (92pt, 1fr), column-gutter: 12pt, row-gutter: 0pt,
      ..range(0, c.len(), step: 2).map(i => (
        grid.cell(inset: (y: 5.5pt), text(weight: "semibold", fill: accent, c.at(i))),
        grid.cell(inset: (y: 5.5pt), c.at(i + 1)),
      )).flatten()))
}

#let couverture(surtitre: [], titre: [], sous-titre: [], auteur: [], date: [], fiche: []) = page(header: none, footer: none, {
  set par(justify: false)
  v(30pt)
  text(font: sans, size: 8.5pt, weight: "semibold", fill: accent, tracking: 1.2pt,
    upper(surtitre))
  v(14pt)
  line(length: 56pt, stroke: 3pt + accent)
  v(16pt)
  block(text(font: serif, size: 25pt, fill: encre, par(leading: 0.42em, titre)))
  v(12pt)
  text(font: serif, size: 14pt, style: "italic", fill: gris, sous-titre)
  v(18pt)
  text(font: sans, size: 9pt)[#text(weight: "semibold", auteur) #h(6pt) · #h(6pt) #date]
  v(1fr)
  fiche
})

#let sommaire() = {
  page(header: none, {
    v(40pt)
    text(font: sans, size: 18pt, weight: "semibold", fill: accent)[Table des matières]
    v(4pt)
    line(length: 100%, stroke: 0.6pt + filet)
    v(10pt)
    set par(justify: false)
    show outline.entry.where(level: 1): it => {
      v(9pt, weak: true)
      text(font: sans, size: 9.5pt, weight: "semibold", fill: accent, it)
    }
    show outline.entry.where(level: 2): set text(font: sans, size: 9pt)
    outline(title: none, depth: 2, indent: 1.2em)
  })
}

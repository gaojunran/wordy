#let data = csv("youdao.csv")
#let _ = data.remove(0)

#table(
  columns: 3,
  [*idx*], [*word*], [*definition*],
  ..data.flatten()
)

// You can add more styles here...
// See more in https://typst.app/docs/reference/model/table/.

interface A {
  log(...args: any): void
  error(...args: any): void
  size: number
}


type Exports = {
  onStart?: () => Promise<void>
  onUpdate: (deltaSeconds: number) => Promise<void>
}

let d: Exports = {
  async onUpdate(d) {},
  async onStart() {}
}

type B = Map<string, Map<string, { timestamp: number, state: string }>>

let b: B = new Map()
let a = 10;
let b = "javascript";
function letScope() {
  let c = 20;
  console.log(c); // 20
}
letScope();
console.log(a); // 10
console.log(b); // javascript
// console.log(c); // ReferenceError: c is not defined

// 局部作用域
// 变量 c 只在函数 letScope 中有效，外部无法访问
// `var`：旧语法，函数作用域，有变量提升、允许重复声明，不推荐现在用
// `let`：块级作用域，可修改，不能重复声明，有暂时性死区
// `const`：块级作用域，常量，不能重新赋值，不能重复声明，有暂时性死区

function learnScope() {
  var gravity = 9.8;
  console.log(gravity); // 9.8
}
learnScope();
// console.log(gravity); // ReferenceError: gravity is not defined

if (true) {
  var gravity = 9.81;
  console.log(gravity); // 9.81   
}
console.log(gravity); // 9.81

for (let i = 0; i < 3; i++) {
  console.log(i); // 0 1 2
}
// console.log(i); // Uncaught ReferenceError: i is not defined
//在 ES6 及更高版本中，我们引入了`let`和`const`，因此您不会再受到`var`的“隐蔽性”影响。使用`let`时，变量的作用域是块级的，不会影响代码的其他部分。 
//` let`和`const` 的作用域相同，区别仅在于是否允许重新赋值。我们不能更改或重新赋值const变量的值。
// 我强烈建议您同时使用` let`和` const`，这样可以编写更简洁的代码，避免难以调试的错误。
// 一般来说，`let`可以用于任何会变化的值，`const`可以用于任何常量值，以及数组、对象、箭头函数和函数表达式。
console.log('-----------------'); 
// object creation
const person = {
  name: 'LudongFang',
  age: 25,
  job: 'developer',
  skills: ['javascript', 'html', 'css'],
  // object methods
  getSkill: function() {
    return this.skills;
  }
}
// object access
console.log(person.name); // LudongFang
console.log(person.age); // 25
console.log(person.job); // developer
console.log(person.getSkill()); // ['javascript', 'html', 'css']
// 为对象设置新属性
person.city = 'Beijing';
console.log(person.city); // Beijing
// 操作对象的方法
const copyPreson = Object.assign({}, person);
console.log(copyPreson); // { name: 'LudongFang', age: 25, job: 'developer', skills: ['javascript', 'html', 'css'], city: 'Beijing' }
//获取对象的键名
console.log(Object.keys(person)); // ['name', 'age', 'job', 'skills', 'city']
//获取对象的value
console.log(Object.values(person)); // ['LudongFang', 25, 'developer', ['javascript', 'html', 'css'], 'Beijing']
//获取对象的键值对
console.log(Object.entries(person)); // [ ['name', 'LudongFang'], ['age', 25], ['job', 'developer'], ['skills', ['javascript', 'html', 'css']], ['city', 'Beijing'] ]
//检查对象是否包含某个属性
console.log(person.hasOwnProperty('name')); // true
console.log(person.hasOwnProperty('age')); // true
console.log(person.hasOwnProperty('work')); // false




















// Vue App ---
let app = new Vue({
    el: '#app',
    delimiters: [
        '[[',
        ']]',
    ],
    data: {
        drinkName: '',
        drinkResults: [],
        drinkResults2: [],

    },
    methods: {
        mergeIngredients: function (drink) {
            let ingredients = []
            for (let i = 1; i <= 15; ++i) {
                let name = drink['strIngredient' + i]
                let amount = drink['strMeasure' + i]
                if (name == null) {
                    break
                }
                if (amount == null) {
                    amount = ''
                }
                ingredients.push({
                    name: name,
                    amount: amount
                })
            }
            return ingredients
        },
        startFind: function () {
            axios({
                method: 'get',
                url: 'https://www.thecocktaildb.com/api/json/v1/1/search.php',
                params: {
                    s: this.drinkName,
                }
            })
                .then((response) => {
                    // if (response.data.drink == null){
                    //     alert('Try again')
                    //     return
                    // }
                    let drink_data = response.data.drinks
                    this.drinkResults = []
                    for (let i = 0; i < drink_data.length; ++i) {
                        this.drinkResults.push({
                            name: drink_data[i].strDrink,
                            instructions: drink_data[i].strInstructions,
                            ingredients: this.mergeIngredients(drink_data[i]),
                            image: drink_data[i].strDrinkThumb,
                        })
                    }

                })
        },
        advancedFind: function (nameChoice) {
            axios({
                method: 'get',
                url: 'https://www.thecocktaildb.com/api/json/v1/1/search.php',
                params: {
                    s: nameChoice,
                }
            }).then((response) => {
                console.log(response.data.drinks)
                let drink_data2 = response.data.drinks
                this.drinkResults2 = []
                for (let i = 0; i < drink_data2.length; ++i) {
                    this.drinkResults2.push({
                        name: drink_data2[i].strDrink,
                        instructions: drink_data2[i].strInstructions,
                        ingredients: this.mergeIngredients(drink_data2[i]),
                        image: drink_data2[i].strDrinkThumb,
                    })
                }

            })

        },
        addDrinkToFavorites: function(drink) {
            console.log(drink)
            axios({
                method: 'post',
                url: "/savetf/",
                data: drink,
                headers: {
                    'X-CSRFToken': '{{csrf_token}}',
                }

            }).then(response =>{
                console.log(response)
            })
        }
    }
});

// end vue
function showCard() {
    document.getElementById('cardHide').setAttribute("class", "card1");
}
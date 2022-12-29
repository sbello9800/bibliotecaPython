        let _btncerrar = document.querySelector("._btncerrar");
        let _btnopen = document.querySelector("._btnopen");
        const _top = document.querySelector("._top")
        

        _btncerrar.addEventListener("click",(e)=>{
            _top.style.animation = "animacion_out 0.5s forwards"
        })
        _btnopen.addEventListener("click",(e)=>{
            _top.style.animation = "animacion_in 0.5s forwards"
            
        })

        let indicador = document.querySelector("#indicador")
        let menu = document.querySelectorAll("._menu ul li a")
        
        menu.forEach( item =>{
            item.addEventListener("mouseover",(e)=>{
                
                indicador.style.top     = item.offsetTop+40+"px"
                indicador.style.width   = item.offsetWidth+"px"
            })
        })

        
        
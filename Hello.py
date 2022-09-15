import streamlit as st
from streamlit.components.v1 import html


st.set_page_config(
    page_icon="🚀",
    page_title= "Vending machines in NYC"
)

st.markdown("# Let's talk vending machines!")

html('''\
<style>
    *{
        padding: 0;
        margin:0;
        box-sizing: border-box;
    }
    .upper-con{
        display: flex;
    }
    .chooser{
        display: grid;
        grid-template-columns: 1fr;
        height: fit-content;
        transform: translateY(100%);
        border: .5rem solid black;
        border-radius: 0 10px 10px 0;
    }
    button{
        height: 2rem;
        width: 8rem;
    }
    button:hover{
        cursor: pointer;
    }

    .container{
        display:grid;
        grid-template-columns: 1fr 1fr 1fr;
        border: 1rem solid black;
        border-bottom: 4rem solid black;
        border-radius: 10px;
        width: fit-content;
    }
    .item{
        width: 10rem;
        height: 12rem;
        position: relative;
        border-bottom: 3px solid black;
        background-color: lightgrey;
    }
    .buy-item{
        position: absolute;
        bottom: 0;
        left:50%;
        transform: translateX(-50%);
        z-index: 1;
    }
    .turner{
        position: absolute;
        z-index: 5;
        bottom: -5%;
        left:50%;
        transform: translateX(-50%) rotate(-40deg);
        transition: transform 1s linear;
    }
    #coke_png{
        transition: transform 1s linear;
    }
    #pepsi_png{
        transition: transform .5s linear;
    }
    #csv-file{
        transition: transform .5s linear;
    }
</style>
<div class="upper-con">
    <div class="container">
        <div class="item">
            <img id="coke_png" class="buy-item" width="140px" src="https://github.com/nilsbayer/Streamlit_Team_2/blob/main/coke.png" alt="">
            <svg class="turner" id="coke-turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg>            
        </div>
        <div class="item">
            <svg class="turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg> 
        </div>
        <div class="item">
            <svg class="turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg> 
        </div>
        <div class="item">
            <svg class="turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg> 
        </div>
        <div class="item">
            <svg class="buy-item" id="csv-file" width="112" height="102" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
                y="0px" viewBox="0 0 303.188 303.188" style="enable-background:new 0 0 303.188 303.188;" xml:space="preserve">
                <g>
                    <polygon style="fill:#E4E4E4;" points="219.821,0 32.842,0 32.842,303.188 270.346,303.188 270.346,50.525 	" />
                    <polygon style="fill:#007934;" points="227.64,25.263 32.842,25.263 32.842,0 219.821,0 	" />
                    <g>
                        <g>
                            <path style="fill:#A4A9AD;" d="M114.872,227.984c-2.982,0-5.311,1.223-6.982,3.666c-1.671,2.444-2.507,5.814-2.507,10.109
                            c0,8.929,3.396,13.393,10.188,13.393c2.052,0,4.041-0.285,5.967-0.856c1.925-0.571,3.86-1.259,5.808-2.063v10.601
                            c-3.872,1.713-8.252,2.57-13.14,2.57c-7.004,0-12.373-2.031-16.107-6.094c-3.734-4.062-5.602-9.934-5.602-17.615
                            c0-4.803,0.904-9.023,2.714-12.663c1.809-3.64,4.411-6.438,7.808-8.395c3.396-1.957,7.39-2.937,11.98-2.937
                            c5.016,0,9.808,1.09,14.378,3.27l-3.841,9.871c-1.713-0.805-3.428-1.481-5.141-2.031
                            C118.681,228.26,116.841,227.984,114.872,227.984z" />
                            <path style="fill:#A4A9AD;" d="M166.732,250.678c0,2.878-0.729,5.433-2.191,7.665c-1.459,2.232-3.565,3.967-6.315,5.205
                            c-2.751,1.237-5.977,1.856-9.681,1.856c-3.089,0-5.681-0.217-7.775-0.65c-2.095-0.434-4.274-1.191-6.538-2.27v-11.172
                            c2.391,1.227,4.877,2.186,7.458,2.872c2.582,0.689,4.951,1.032,7.109,1.032c1.862,0,3.227-0.322,4.095-0.969
                            c0.867-0.645,1.302-1.476,1.302-2.491c0-0.635-0.175-1.19-0.524-1.666c-0.349-0.477-0.91-0.958-1.682-1.444
                            c-0.772-0.486-2.83-1.48-6.173-2.983c-3.026-1.375-5.296-2.708-6.809-3.999s-2.634-2.771-3.364-4.443s-1.095-3.65-1.095-5.936
                            c0-4.273,1.555-7.605,4.666-9.997c3.109-2.391,7.384-3.587,12.822-3.587c4.803,0,9.7,1.111,14.694,3.333l-3.841,9.681
                            c-4.337-1.989-8.082-2.984-11.234-2.984c-1.63,0-2.814,0.286-3.555,0.857s-1.111,1.28-1.111,2.127
                            c0,0.91,0.471,1.725,1.412,2.443c0.941,0.72,3.496,2.031,7.665,3.936c3.999,1.799,6.776,3.729,8.331,5.792
                            C165.955,244.949,166.732,247.547,166.732,250.678z" />
                            <path style="fill:#A4A9AD;" d="M199.964,218.368h14.027l-15.202,46.401H184.03l-15.139-46.401h14.092l6.316,23.519
                            c1.312,5.227,2.031,8.865,2.158,10.918c0.148-1.481,0.443-3.333,0.889-5.555c0.443-2.222,0.835-3.967,1.174-5.236
                            L199.964,218.368z" />
                        </g>
                    </g>
                    <polygon style="fill:#D1D3D3;" points="219.821,50.525 270.346,50.525 219.821,0 	" />
                    <g>
                        <rect x="134.957" y="80.344" style="fill:#007934;" width="33.274" height="15.418" />
                        <rect x="175.602" y="80.344" style="fill:#007934;" width="33.273" height="15.418" />
                        <rect x="134.957" y="102.661" style="fill:#007934;" width="33.274" height="15.419" />
                        <rect x="175.602" y="102.661" style="fill:#007934;" width="33.273" height="15.419" />
                        <rect x="134.957" y="124.979" style="fill:#007934;" width="33.274" height="15.418" />
                        <rect x="175.602" y="124.979" style="fill:#007934;" width="33.273" height="15.418" />
                        <rect x="94.312" y="124.979" style="fill:#007934;" width="33.273" height="15.418" />
                        <rect x="134.957" y="147.298" style="fill:#007934;" width="33.274" height="15.418" />
                        <rect x="175.602" y="147.298" style="fill:#007934;" width="33.273" height="15.418" />
                        <rect x="94.312" y="147.298" style="fill:#007934;" width="33.273" height="15.418" />
                        <g>
                            <path style="fill:#007934;" d="M127.088,116.162h-10.04l-6.262-10.041l-6.196,10.041h-9.821l10.656-16.435L95.406,84.04h9.624
                            l5.8,9.932l5.581-9.932h9.909l-10.173,16.369L127.088,116.162z" />
                        </g>
                    </g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
            </svg>
            <svg class="turner" id="csv-turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg>  
        </div>
        <div class="item">
            <img id="pepsi_png" class="buy-item" width="140px" src="https://github.com/nilsbayer/Streamlit_Team_2/blob/main/pepsi.png" alt="">
            <svg class="turner" id="pepsi-turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg> 
        </div>
        <div class="item">
            <img class="buy-item" width="140px" src="https://github.com/nilsbayer/Streamlit_Team_2/blob/main/coke.png" alt="">
            <svg class="turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg> 
        </div>
        <div class="item">
            <svg class="turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg> 
        </div>
        <div class="item">
            <img class="buy-item" width="140px" src="https://github.com/nilsbayer/Streamlit_Team_2/blob/main/pepsi.png" alt="">
            <svg class="turner" width="78.4" height="71.4" viewBox="0 0 112 102" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="turner" d="M6 46C6 73.6142 28.3858 96 56 96C83.6142 96 106 73.6142 106 46C106 18.3858 85 8 81 5" stroke="#606060" stroke-width="16"/>
            </svg> 
        </div>
    </div>
    <div class="chooser">
        <button id="coke-btn">COKE - 15 DKK</button>
        <button id="pep-btn">PEPSI - 15 DKK</button>
        <button id="csv-btn">CSV - 150 DKK</button>
    </div>
</div>
<script>
    const cokeBtn = document.getElementById("coke-btn")
    const pepsiBtn = document.getElementById("pep-btn")
    const csvBtn = document.getElementById("csv-btn")

    cokeBtn.addEventListener("click", () => {
        document.getElementById("coke-turner").style.transform = "translateX(-50%) rotate(40deg)"
        setTimeout(() => {
            document.getElementById("coke_png").style.transform = "translateX(-50%) translateY(300%) rotate(10deg)"
        }, 1000)
        setTimeout(() => {
            document.getElementById("coke_png").style.display = "none"
        }, 2000)
    })
    pepsiBtn.addEventListener("click", () => {
        document.getElementById("pepsi-turner").style.transform = "translateX(-50%) rotate(40deg)"
        setTimeout(() => {
            document.getElementById("pepsi_png").style.transform = "translateX(-50%) translateY(150%) rotate(10deg)"
        }, 1000)
        setTimeout(() => {
            document.getElementById("pepsi_png").style.display = "none"
        }, 1500)
    })
    csvBtn.addEventListener("click", () => {
        document.getElementById("csv-turner").style.transform = "translateX(-50%) rotate(40deg)"
        setTimeout(() => {
            document.getElementById("csv-file").style.transform = "translateX(-50%) translateY(200%) rotate(10deg)"
        }, 1000)
        setTimeout(() => {
            document.getElementById("csv-file").style.display = "none"
        }, 1500)
    })
</script>    
''')

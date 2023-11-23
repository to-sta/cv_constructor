<script lang="ts">

</script>


<!-- EXAMPLE CV
https://img.freepik.com/freie-psd/saubere-und-moderne-lebenslauf-oder-lebenslaufvorlage_237398-297.jpg?w=996&t=st=1688998846~exp=1688999446~hmac=0da6a030eec9a51ead50e096de88765ffc3a7c607e21a4c82468ad1549d9423e
-->


    <!-- DIN A4   -->
    <main style="min-width: 21cm; min-height: 29.7cm" class="relative ">
      <!-- Colums -->
      <div class="absolute top-0 bottom-0 left-0 right-0 flex">
        <!-- Left Side -->
        <aside class="flex flex-col w-1/3 h-full gap-4 text-white bg-gray-800/90">
          <img alt="potrait" class="object-cover h-96" src="https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80">
          <!-- Education  -->
          <div id="Education" class="pt-4 pl-6">
            <h1 class="pb-2 text-lg font-bold uppercase border-b-2 border-yellow-400">Education</h1>
            <ul class="pt-4 pl-2">
              <li>
                <h1 class="font-semibold uppercase">Enter your mayor</h1>
                <h2 class="text-sm">Name of Your University</h2>
                <h2 class="text-sm">2005-2009</h2>
              </li>
            </ul>
            <ul class="pt-4 pl-2">
              <li>
                <h1 class="font-semibold uppercase">Enter your mayor</h1>
                <h2 class="text-sm">Name of Your University</h2>
                <h2 class="text-sm">2009-2011</h2>
              </li>
            </ul>
            <!-- Reference  -->
          </div>
          <div id="Reference" class="pl-6">
            <h1 class="pb-2 text-lg font-bold uppercase border-b-2 border-yellow-400">Reference</h1>
            <ul class="pt-4 pl-2">
              <li>
                <h1 class="font-semibold uppercase">Sara Taylore</h1>
                <h2 class="text-sm">Director | Company Name</h2>
                <h2 class="text-sm">T: +1 234 56789</h2>
              </li>
            </ul>
            <ul class="pt-4 pl-2">
              <li>
                <h1 class="font-semibold uppercase">Micke Anderson</h1>
                <h2 class="text-sm">Webdeveloper</h2>
                <h2 class="text-sm">T: +1 234 56789</h2>
              </li>
            </ul>
          </div>

          <!-- Personal Details -->
          <div class="pt-6">
            <!-- Phone -->
            <div class="flex flex-row h-6">
              <div class="w-1/4 bg-yellow-400"></div>
              <div class="w-3/4 pl-4 font-bold bg-gray-600">Phone</div>
            </div>
            <div class="flex flex-row h-6">
              <div class="w-1/4"></div>
              <div class="w-3/4 pl-4 text-sm">+000 123 456 789</div>
            </div>
            <!-- Email-->
            <div class="flex flex-row h-6">
              <div class="w-1/4 bg-yellow-400"></div>
              <div class="w-3/4 pl-4 font-bold bg-gray-600">Email</div>
            </div>
            <div class="flex flex-row h-6">
              <div class="w-1/4"></div>
              <div class="w-3/4 pl-4 text-sm">yourname@gmail.com</div>
            </div>
            <!-- website -->
            <div class="flex flex-row h-6">
              <div class="w-1/4 bg-yellow-400"></div>
              <div class="w-3/4 pl-4 text-sm font-bold bg-gray-600">Website</div>
            </div>
            <div class="flex flex-row h-6">
              <div class="w-1/4"></div>
              <div class="w-3/4 pl-4 text-sm">yourwebsitename.com</div>
            </div>
            <!-- Address -->
            <div class="flex flex-row h-6">
              <div class="w-1/4 bg-yellow-400"></div>
              <div class="w-3/4 pl-4 font-bold bg-gray-600">Address</div>
            </div>
            <div class="flex flex-row h-6">
              <div class="w-1/4"></div>
              <div class="w-3/4 pl-4 text-sm">your street address</div>
            </div>
            <div class="flex flex-row h-6">
              <div class="w-1/4"></div>
              <div class="w-3/4 pl-4 text-sm">City/Zip Code - 456</div>
            </div>
          </div>
        </aside>

        <!-- Right Side -->
        <div class="flex flex-col w-2/3 h-full bg-gray-400/20">
          <div class="w-full">
            <!-- Header/Banner -->
            <ul class="py-8 pl-10 mt-20 bg-yellow-400">
              <h1 class="text-4xl"><b>Karen</b> Richards</h1>
              <h2 class="text-2xl">Professional Title</h2>
            </ul>

            <!-- Content Section -->
            <section class="flex flex-col gap-8 px-10 pt-8">
              <!-- About me -->
              <div class="flex flex-col gap-3">
                <h1 class="text-xl uppercase border-b-4 border-gray-400">About me</h1>
                <p class="text-sm">
                  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
                </p>
              </div>

              <!-- Work Experience -->
              <div class="flex flex-col gap-3">
                <!-- Headline -->
                <h1 class="text-xl uppercase border-b-4 border-gray-400">Work Experience</h1>

                <div id="exp_blocks" class="flex flex-col gap-4">
                  <!-- Block 1 -->
                  <div class="flex">
                    <div class="w-1/3">
                      <p>2012-2014</p>
                    </div>
                    <div class="w-2/3">
                      <h1 class="font-semibold uppercase text-md">job position</h1>
                      <h2 class="text-sm font-semibold">Company Name/ California USA</h2>
                      <p class="pt-3 text-sm">
                        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
                      </p>
                    </div>
                  </div>

                  <!-- Block 2 -->
                  <div class="flex">
                    <div class="w-1/3">
                      <p>2012-2014</p>
                    </div>
                    <div class="w-2/3">
                      <h1 class="font-semibold uppercase text-md">job position</h1>
                      <h2 class="text-sm font-semibold">Company Name/ California USA</h2>
                      <p class="pt-3 text-sm">
                        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
                      </p>
                    </div>
                  </div>

                  <!-- Block 3 -->
                  <div class="flex">
                    <div class="w-1/3">
                      <p>2012-2014</p>
                    </div>
                    <div class="w-2/3">
                      <h1 class="font-semibold uppercase text-md">job position</h1>
                      <h2 class="text-sm font-semibold">Company Name/ California USA</h2>
                      <p class="pt-3 text-sm">
                        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
                      </p>
                    </div>
                  </div>

                </div>
              </div>

              <!-- About me -->
              <div class="flex flex-col gap-3">
                <h1 class="text-xl uppercase border-b-4 border-gray-400">Software Skills</h1>
                <div class="flex">
                  <!-- Empty -->
                  <div class="w-1/3"></div>
                  <!-- 2 Columns -->

                  <div class="flex flex-row w-2/3 text-sm">
                    <!-- First Row  -->

                    <div class="w-1/2">
                      <ul class="py-2">
                        <li>Adobe Photoshop</li>
                        <li class="flex w-full h-1 pr-6 mt-2">
                          <div class="w-3/4 bg-gray-500"></div>
                          <div class="w-1/4 bg-gray-300"></div>
                        </li>
                      </ul>
                      <ul class="py-2">
                        <li>Adobe Illustrator</li>
                        <li class="flex w-full h-1 pr-6 mt-2">
                          <div class="w-3/4 bg-gray-500"></div>
                          <div class="w-1/4 bg-gray-300"></div>
                        </li>
                      </ul>
                      <ul class="py-2">
                        <li>Adobe Indesign</li>
                        <li class="flex w-full h-1 pr-6 mt-2">
                          <div class="w-3/4 bg-gray-500"></div>
                          <div class="w-1/4 bg-gray-300"></div>
                        </li>
                      </ul>
                    </div>
                    <div class="w-1/2">
                      <ul class="py-2">
                        <li>Microsoft Word</li>
                        <li class="flex w-full h-1 pr-6 mt-2">
                          <div class="w-3/4 bg-gray-500"></div>
                          <div class="w-1/4 bg-gray-300"></div>
                        </li>
                      </ul>
                      <ul class="py-2">
                        <li>Microsoft Powerpoint</li>
                        <li class="flex w-full h-1 pr-6 mt-2">
                          <div class="w-3/4 bg-gray-500"></div>
                          <div class="w-1/4 bg-gray-300"></div>
                        </li>
                      </ul>
                      <ul class="py-2">
                        <li>HTML/CSS</li>
                        <li class="flex w-full h-1 pr-6 mt-2">
                          <div class="w-3/4 bg-gray-500"></div>
                          <div class="w-1/4 bg-gray-300"></div>
                        </li>
                      </ul>
                    </div>
                  </div>


                </div>

              </div>

            </section>

          </div>
        </div>

      </div>
    </main>

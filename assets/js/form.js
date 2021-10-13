
        $(document).ready(function () {
            $("#signupform").hide();
            $(".signUp").click(function () {
                $("#signupform").show();
                $("#signinform").hide();
            });


            $("#signin").click(function () {
                $("#signupform").hide();
                $("#signinform").show();
            });

        });

        $(document).ready(function () {
            $(".item-first").addClass("list-item-first")

            $(".item-second").click(function () {
                $(this).addClass("list-item-first")
                $(".item-first").removeClass("list-item-first")

            });

            $(".item-first").click(function () {
                $(this).addClass("list-item-first")
                $(".item-second").removeClass("list-item-first")

            });





        });

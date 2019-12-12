<html>
    <head>
        <title>Darren's Photo Frame</title>
    </head>
    <body bgcolor="grey" style="margin:4; padding:5" link="blue" vlink="blue">
        <?php
            $thisfile = basename($_SERVER['SCRIPT_FILENAME']);
            $value = $_GET['value'];
            $images = glob("FramePictures/*.{jpeg,JPEG,jpg,JPG,png,PNG,tif,TIF,tiff,TIFF}", GLOB_BRACE); 
            #print_r($images);

            #Table structure and links to repoert types
            echo "<table bgcolor=\"white\" style=\"width:900px\" align=\"center\"><tr><td>";
            echo "<center>";
            echo "<h1>Darren's Photo Frame<hr width=\"700px\"></h1>";
            #echo "<h2><a href=" . $thisfile . "?value=exit>Exit</a></h2>";
            #echo "<hr width=\"400px\">";
            #echo "<h2><a href=" . $thisfile . "?value=start>Start</a></h2>";
            #echo "<p><a href=" . $thisfile . "?value=next>Next Image</a></p>";

            echo "<p>";
            $br = 0;
            foreach ($images as $image) {
                $br = $br + 1;
                $image = str_replace("FramePictures/","",$image);
                $imageUrl = str_replace(" ", "%20",$image);
                $thumb = "FramePictures/Thumbs/".$image;
                if (file_exists($thumb)) {
                }else {
                    echo exec("python home/CreateThumbs.pyw $image");
                }
                echo '<a href=' . $thisfile . '?value=/home/pi/Pictures/'.$imageUrl.'><img src="'.$thumb.'" width="260" height="140" hspace="10"></a>';

                 if ($br == 3) {
                     $br = 0;
                     echo "</p><p>";
                 }
            }

            echo "</center></tr></td></table>";

            if ($value != "") {
                if ($value == "exit") {
                    $myfile = fopen("home/UpdatePhotoFrame.txt", "w");
                    fwrite($myfile, "exit");
                    fclose($myfile);
                }elseif ($value == "next") {
                    $myfile = fopen("home/UpdatePhotoFrame.txt", "w");
                    fwrite($myfile, "next");
                    fclose($myfile);
                }else {
                    $myfile = fopen("home/UpdatePhotoFrame.txt", "w");
                    $value = str_replace("%20"," ",$value);
                    fwrite($myfile, $value);
                    fclose($myfile);
                }
            }
        ?>
    </body>
</html>

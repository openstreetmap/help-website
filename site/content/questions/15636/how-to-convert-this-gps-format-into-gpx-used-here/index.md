+++
type = "question"
title = "How to convert this GPS Format into GPX used here"
description = '''Hi dear community - I am new here and I use a older version (1.02) of &quot;BeeLineGPS&quot;. After the first test with this tracking software I get a logfile like this : $GPGSA,A,3,15,18,17,09,12,27,,,,,,,2.4,1.6,1.83E $GPRMC,074917.000,A,4905.3612,N,00924.2183,E,0.00,,290812,,,A75 : $GPGSA,A,3,15,09,12,27,,...'''
date = "2012-08-29T11:00:00Z"
lastmod = "2012-08-31T22:38:00Z"
weight = 15636
keywords = [ "convert", "gpx", "gpgsa" ]
aliases = [ "/questions/15636" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert this GPS Format into GPX used here](/questions/15636/how-to-convert-this-gps-format-into-gpx-used-here)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15636-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi dear community - I am new here and I use a older version (1.02) of "BeeLineGPS". After the first test with this tracking software I get a logfile like this :</p>
<p>$GPGSA,A,3,15,18,17,09,12,27,,,,,,,2.4,1.6,1.8<em>3E $GPRMC,074917.000,A,4905.3612,N,00924.2183,E,0.00,,290812,,,A</em>75<br />
:<br />
$GPGSA,A,3,15,09,12,27,,,,,,,,,2.5,2.2,1.0<em>3F $GPRMC,082444.000,A,4905.4403,N,00924.2823,E,1.08,114.07,290812,,,A</em>65</p>
<p>As I would like to use this older registered software, I would like to know, how to convert this file to a up loadable format used by open street map.</p>
<p>At the moment I don´t want to spend money without knowing more about this subject. Are they any converters to solve the problem?</p>
<p>Thanks &amp; Regards Yougy2</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-gpgsa" rel="tag" title="see questions tagged &#39;gpgsa&#39;">gpgsa</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '12, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/1ee2df2b55b72ee6195175a4317a1ecd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yougy2&#39;s gravatar image" />
<p><span>Yougy2</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yougy2 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '12, 19:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-15636" class="comments-container">
<span id="15648"></span>
<div id="comment-15648" class="comment">
<div id="post-15648-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you both for the quick answer ! Have downloaded gpsbabel and looked up the setup.</p>
<p>Have located GPX XML (gpx) and NMEA 0183 sentences (nmea) Hope this have been the correct selection. Left all to default.</p>
<p>Input file has been a txt-file as copied off the GPS Unit Output NMEA 0183 sentences (nmea)</p>
<p>Used gpsbabel to get the following msg.:</p>
<pre><code>gpsbabel -w -t -i nmea,gprmc=0,gpgga=0,gpvtg=0,gpgsa=0,get_posn=0,append_positioning=0,gisteq=0 -f C:\Users\Spiess\Desktop\new file.txt -o nmea,gprmc=0,gpgga=0,gpvtg=0,gpgsa=0,get_posn=0,append_positioning=0,gisteq=0 -F &quot;C:\Users\Spiess\Desktop\newgpx file
nmea cannot open &#39;&quot;C:\Users\Spiess\Desktop\newgpx file&#39; for write.  Error was &#39;Invalid argument&#39;.</code></pre>
<p>Any ideas? There was an Error executing gpsbabel, Proccess ended with Error 1.</p>
<p>Regards &amp; Thanks Yougy2</p>
</div>
<div id="comment-15648-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 13:07)</span> <span class="comment-user userinfo">Yougy2</span>
</div>
</div>
<span id="15649"></span>
<div id="comment-15649" class="comment">
<div id="post-15649-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It looks like you've got spaces in file names, but haven't quoted the file name. Instead of using:</p>
<p>new file.txt</p>
<p>use</p>
<p>"new file.txt"</p>
<p>or perhaps better:</p>
<p>newfile.txt</p>
</div>
<div id="comment-15649-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 13:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15650"></span>
<div id="comment-15650" class="comment">
<div id="post-15650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Thanks ... Have done the changes - File for Input now -- "C:UsersmeDesktopnewfile.txt" NMEA 0183 sentences (nmea)</p>
<p>Unchanged Optios: gprmc=0,gpgga=0,gpvtg=0,gpgsa=0,get_posn=0,append_positioning=0,gisteq=0</p>
<p>File for output, unchanged -- "C:meSpiessDesktopnewgpx file GPX XML</p>
<p>Unchanged options: suppresswhite=0,logpoint=0,humminbirdextensions=0,garminextensions=0</p>
<p>Error : gpsbabel -w -t -i nmea,gprmc=0,gpgga=0,gpvtg=0,gpgsa=0,get_posn=0,append_positioning=0,gisteq=0 -f "C:UsersmeDesktopnewfile.txt" -o gpx,suppresswhite=0,logpoint=0,humminbirdextensions=0,garminextensions=0 -F "C:UsersmeDesktopnewgpx file nmea: Cannot open file '"C:UsersmeDesktopnewfile.txt"'!</p>
<p>Error executing gpsbabel: Prozess end with code 1</p>
<p>Any other ideas ? Thanks, Regards Yougy2</p>
</div>
<div id="comment-15650-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 13:27)</span> <span class="comment-user userinfo">Yougy2</span>
</div>
</div>
<span id="15651"></span>
<div id="comment-15651" class="comment not_top_scorer">
<div id="post-15651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just have seen there is a option to send a screen shot. Ad this now to the question / reply sent already.</p>
<p><img src="/upfiles/GPSBabel-1.4.3,_Pic1.jpg" alt="alt text" /></p>
<p>Hope this works - I am a New User here ...</p>
<p>Thanks &amp; Regards Yougy2</p>
</div>
<div id="comment-15651-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 13:38)</span> <span class="comment-user userinfo">Yougy2</span>
</div>
</div>
<span id="15717"></span>
<div id="comment-15717" class="comment not_top_scorer">
<div id="post-15717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dear Community, as stated, the converted "Example.gpx" has been uploaded. At least visible entry in "mytracks". The map seems to be the right area, but I am unable to identify my uploaded track.</p>
<p>Enclose the file details -</p>
<p>Dateiname: Example.gpx (herunterladen) Hochgeladen am: 31. August 2012 um 10:10 Punkte: 2,004 Startkoordinate: 49.0894; 9.40364 (Karte / bearbeiten) Besitzer: Yougy2 Beschreibung: Ein Test einer Fahrstrecke - Erstuser Tags: Keine Sichtbarkeit: Identifizierbar (wird in der Trackliste als sortierte Punktfolge mit Zeitstempel angezeigt)</p>
<p>How I am able to identify this track ? Potlach is just showing loads of tracks, without any chance identifying my own to check or work on it.</p>
<p>Thanks for the help and support Yougy2</p>
</div>
<div id="comment-15717-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 11:54)</span> <span class="comment-user userinfo">Yougy2</span>
</div>
</div>
<span id="15718"></span>
<div id="comment-15718" class="comment not_top_scorer">
<div id="post-15718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In Potlatch2 at the top click on GPS, My Tracks, Refresh list, then click on the track you are editing from.</p>
</div>
<div id="comment-15718-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 12:43)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="15719"></span>
<div id="comment-15719" class="comment not_top_scorer">
<div id="post-15719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you found a very faint colored tack, only visible, when no other tacks are next to it. Deleted it again to do a better one.</p>
<p>Is there a off-line software to be used ? And how I get my uploaded track better visible to work on it ?</p>
<p>Thanks, Regards Yougy2</p>
</div>
<div id="comment-15719-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 12:58)</span> <span class="comment-user userinfo">Yougy2</span>
</div>
</div>
<span id="15720"></span>
<div id="comment-15720" class="comment">
<div id="post-15720-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>software to do what? Ideally, as your original question as been answered you should accept the answer you think best, award points where earned. then ask a new clear separate question. So that users can search questions easily and quickly go the the best answer.</p>
</div>
<div id="comment-15720-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 13:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="15721"></span>
<div id="comment-15721" class="comment">
<div id="post-15721-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm sure that you're already aware, but just in case you are not - you'll need to edit the map to reflect the trace that you've uploaded - an uploaded GPS trace doesn't magically become a cycleway, for example. There's an introductory series of pages on the wiki <a href="https://wiki.openstreetmap.org/wiki/Beginner%27s_Guide">here</a> (und <a href="https://wiki.openstreetmap.org/wiki/DE:Beginners%27_guide">auf Deutsch</a>).</p>
</div>
<div id="comment-15721-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 13:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15727"></span>
<div id="comment-15727" class="comment not_top_scorer">
<div id="post-15727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for all the Support to all here !! Was grate !! Managed to upload an locating the Track on screen. The problem was, that the upload track gets displayed in some sort light blue. Difficult to see on a laptop.</p>
<p>Thanks Yougy2</p>
</div>
<div id="comment-15727-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 18:50)</span> <span class="comment-user userinfo">Yougy2</span>
</div>
</div>
<span id="15732"></span>
<div id="comment-15732" class="comment not_top_scorer">
<div id="post-15732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I must admit that until I messed around with screen brightness and put on spectacles I found the light blue less than ideal.</p>
</div>
<div id="comment-15732-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 22:22)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="15735"></span>
<div id="comment-15735" class="comment not_top_scorer">
<div id="post-15735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you select "Map Style" (at the top right) you might find that one of the other options (besides the default "Potlatch") might contrast better with the light blue. There isn't a built-in map style that uses something other than light blue for GPS traces, though.</p>
</div>
<div id="comment-15735-info" class="comment-info">
<span class="comment-age">(31 Aug '12, 22:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15636" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-15636-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15643"></span>

<div id="answer-container-15643" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15643-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That looks like NMEA format to me. Since NMEA and GPX are both widely supported standards, almost any computer mapping or GPS application will probably be able to import a file in NMEA format and export the data in GPX format. If you don't have any such application already installed, try Andy Mackey's suggestion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</img>
</div>
</div>
<div id="comments-container-15643" class="comments-container">
&#10;</div>
<div id="comment-tools-15643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15643-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15659"></span>

<div id="answer-container-15659" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15659-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This worked for me:</p>
<p>gpsbabel -i nmea -f "C:Example.nmea" -o gpx -F "C:Example.gpx".</p>
<p>The file that I had re-named as C:Example was a NMEA file downloaded from the internet. I would have used your example, but it seems to have shrunk. The GPX file that gpsbabel created was successfully opened and plotted by two other applications, including MapSource, which I have found to be rather unwilling to accept GPX files containing errors.</p>
<p>Once you have got that working, you could try adding the command line options one by one, but you probably don't need them. If you just want to upload the file to OSM, any GPX file should suffice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15659" class="comments-container">
<span id="15677"></span>
<div id="comment-15677" class="comment">
<div id="post-15677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for all the help !! Looks like some conversion has been done using a BAT File as suggested by Madryn. Hope I have done it correctly awarding some points ...</p>
<p>gpsbabel -i nmea -f "C:Example.nmea" -o gpx -F "C:Example.gpx".</p>
<p>helped changing it a little for my setup here. The input file created by the old version of BeeLineGPS is a TXT-File! This is why the conversion of GPS Babel did not worked. It´s silly I have not recognized this in the first place - sorry.</p>
<p>Have only converted the TXT to a GPX</p>
<p>TXT - File:</p>
<p>$GPGSA,A,3,15,18,17,09,12,27,,,,,,,2.4,1.6,1.8<em>3E $GPRMC,074917.000,A,4905.3612,N,00924.2183,E,0.00,,290812,,,A</em>75 $GPGGA,074918.000,4905.3612,N,00924.2183,E,1,05,1.8,471.1,M,48.0,M,,0000<em>55 $GPGSA,A,3,15,18,17,12,27,,,,,,,,2.8,1.8,2.2</em>3C $GPRMC,074918.000,A,4905.3612,N,00924.2183,E,0.00,,290812,,,A<em>7A $GPGGA,074919.000,4905.3612,N,00924.2183,E,1,06,1.6,471.1,M,48.0,M,,0000</em>59 $GPGSA,A,3,15,18,17,09,12,27,,,,,,,2.4,1.6,1.8<em>3E $GPRMC,074919.000,A,4905.3612,N,00924.2183,E,0.00,,290812,,,A</em>7B $GPGGA,074920.000,4905.3612,N,00924.2183,E,1,04,9.1,471.1,M,48.0,M,,0000<em>5E $GPGSA,A,3,18,17,09,12,,,,,,,,,9.5,9.1,2.8</em>39 $GPGSV,3,1,12,09,84,023,24,27,75,090,16,31,59,297,,26,57,288,<em>75 $GPGSV,3,2,12,12,50,241,33,16,49,236,,15,38,182,,17,33,055,24</em>73 $GPGSV,3,3,12,22,17,300,33,18,12,255,33,30,10,242,,28,07,058,<em>71 $GPRMC,074920.000,A,4905.3612,N,00924.2183,E,0.00,,290812,,,A</em>71 $GPGGA,074921.000,4905.3612,N,00924.2183,E,1,06,1.6,471.1,M,48.0,M,,0000*52 .... .... looks now like :</p>
<p>&lt;gpx version="1.0" creator="GPSBabel - &amp;lt;a href=" http:="" www.gpsbabel.org"=""&gt;http://www.gpsbabel.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/0" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 <a href="http://www.topografix.com/GPX/1/0/gpx.xsd">"&gt;http://www.topografix.com/GPX/1/0/gpx.xsd"&gt;</a> &lt;time&gt;2012-08-30T11:33:41Z&lt;/time&gt; &lt;bounds minlat="49.089228333" minlon="9.403351667" maxlat="49.090763333" maxlon="9.406095000"/&gt; &lt;trk&gt; &lt;trkseg&gt; &lt;trkpt lat="49.089353333" lon="9.403638333"&gt; &lt;time&gt;2012-08-29T07:49:17Z&lt;/time&gt; &lt;course&gt;0.000000&lt;/course&gt; &lt;speed&gt;0.000000&lt;/speed&gt; &lt;/trkpt&gt; &lt;trkpt lat="49.089353333" lon="9.403638333"&gt; &lt;ele&gt;471.100000&lt;/ele&gt; &lt;time&gt;2012-08-29T07:49:18Z&lt;/time&gt; &lt;course&gt;0.000000&lt;/course&gt; &lt;speed&gt;0.000000&lt;/speed&gt; &lt;fix&gt;3d&lt;/fix&gt; &lt;sat&gt;5&lt;/sat&gt; &lt;hdop&gt;1.800000&lt;/hdop&gt; &lt;vdop&gt;2.200000&lt;/vdop&gt; &lt;pdop&gt;2.800000&lt;/pdop&gt; &lt;/trkpt&gt; &lt;trkpt lat="49.089353333" lon="9.403638333"&gt; &lt;ele&gt;471.100000&lt;/ele&gt; &lt;time&gt;2012-08-29T07:49:19Z&lt;/time&gt; &lt;course&gt;0.000000&lt;/course&gt; &lt;speed&gt;0.000000&lt;/speed&gt; &lt;fix&gt;3d&lt;/fix&gt; &lt;sat&gt;6&lt;/sat&gt; &lt;hdop&gt;1.600000&lt;/hdop&gt; &lt;vdop&gt;1.800000&lt;/vdop&gt; &lt;pdop&gt;2.400000&lt;/pdop&gt; &lt;/trkpt&gt; &lt;trkpt lat="49.089353333" lon="9.403638333"&gt; &lt;ele&gt;471.100000&lt;/ele&gt; &lt;time&gt;2012-08-29T07:49:20Z&lt;/time&gt; &lt;course&gt;0.000000&lt;/course&gt; &lt;speed&gt;0.000000&lt;/speed&gt; &lt;fix&gt;3d&lt;/fix&gt; &lt;sat&gt;4&lt;/sat&gt; &lt;hdop&gt;9.100000&lt;/hdop&gt; &lt;vdop&gt;2.800000&lt;/vdop&gt; &lt;pdop&gt;9.500000&lt;/pdop&gt; &lt;/trkpt&gt; &lt;trkpt lat="49.089353333" lon="9.403638333"&gt; &lt;ele&gt;471.100000&lt;/ele&gt; &lt;time&gt;2012-08-29T07:49:21Z&lt;/time&gt; &lt;course&gt;0.000000&lt;/course&gt; &lt;speed&gt;0.000000&lt;/speed&gt; &lt;fix&gt;3d&lt;/fix&gt; &lt;sat&gt;6&lt;/sat&gt; &lt;hdop&gt;1.600000&lt;/hdop&gt; &lt;vdop&gt;1.800000&lt;/vdop&gt; &lt;pdop&gt;2.400000&lt;/pdop&gt; &lt;/trkpt&gt; &lt;trkpt lat="49.089353333" lon="9.403638333"&gt; &lt;ele&gt;471.100000&lt;/ele&gt; &lt;time&gt;2012-08-29T07:49:22Z&lt;/time&gt; &lt;course&gt;0.000000&lt;/course&gt; &lt;speed&gt;0.000000&lt;/speed&gt; &lt;fix&gt;3d&lt;/fix&gt; &lt;sat&gt;6&lt;/sat&gt; &lt;hdop&gt;1.600000&lt;/hdop&gt; &lt;vdop&gt;1.800000&lt;/vdop&gt; &lt;pdop&gt;2.400000&lt;/pdop&gt; &lt;/trkpt&gt; &lt;trkpt lat="49.089353333" lon="9.403638333"&gt; &lt;ele&gt;471.100000&lt;/ele&gt; &lt;time&gt;2012-08-29T07:49:23Z&lt;/time&gt; &lt;course&gt;0.000000&lt;/course&gt; &lt;speed&gt;0.000000&lt;/speed&gt; &lt;fix&gt;3d&lt;/fix&gt; ... ...</p>
<p>Now I Look into how to upload the file into openstreetmap to find out how I get further. Will wait a few days, in case I do something wrong trying this file "life".</p>
<p>Don´t want to do something silly or damage the system. So your checkup would be highly appreciated.</p>
<p>Now I read the suggested link <a href="https://wiki.openstreetmap.org/wiki/Recording_GPS_tracks.">https://wiki.openstreetmap.org/wiki/Recording_GPS_tracks.</a></p>
<p>Thanks to all ...</p>
</div>
<div id="comment-15677-info" class="comment-info">
<span class="comment-age">(30 Aug '12, 12:56)</span> <span class="comment-user userinfo">Yougy2</span>
</div>
</div>
<span id="15678"></span>
<div id="comment-15678" class="comment">
<div id="post-15678-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can award points, but it's also helpful to "mark this answer as accepted answer" so that the question appears as "answered" (which also awards 15 points).</p>
</div>
<div id="comment-15678-info" class="comment-info">
<span class="comment-age">(30 Aug '12, 13:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15699"></span>
<div id="comment-15699" class="comment">
<div id="post-15699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A GPX file has to start with a line something like</p>
<p>"&lt;?xml version="1.0" encoding="UTF-8"?&gt;"</p>
<p>Perhaps something went wrong when you copied the file here, because when I took your NMEA data and ran it through GPS Babel as described, it produced a valid GPX file, although obviously containing only a few points.</p>
<p>Try uploading the complete GPX file to OSM. It should be accepted, and I am sure that the OSM programmers have ensured that you cannot damage anything by making a simple mistake, such as uploading the wrong file. You can delete an uploaded trace from OSM if you don't like it.</p>
</div>
<div id="comment-15699-info" class="comment-info">
<span class="comment-age">(30 Aug '12, 22:25)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
</div>
<div id="comment-tools-15659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15659-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15642"></span>

<div id="answer-container-15642" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is used by some OSMers <a href="http://www.gpsbabel.org/capabilities.html">http://www.gpsbabel.org/capabilities.html</a> more info</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Recording_GPS_tracks">https://wiki.openstreetmap.org/wiki/Recording_GPS_tracks</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 12:25</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '12, 12:55</strong> </span></p>
</div>
</div>
<div id="comments-container-15642" class="comments-container">
<span id="15646"></span>
<div id="comment-15646" class="comment">
<div id="post-15646-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BeeLineGPS seems to be software, so what is the hardware are you using to record the trace in the first place it may be easier to use some other software directly in future if you can't convert it, unless you wish to convert some previously recorded beelinegps files that you have already.</p>
</div>
<div id="comment-15646-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 12:46)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-15642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15642-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


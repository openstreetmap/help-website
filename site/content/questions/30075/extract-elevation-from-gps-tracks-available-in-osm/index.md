+++
type = "question"
title = "Extract Elevation from GPS tracks available in OSM"
description = '''I intend to extract Elevation from GPS tracks available in OSM I´m trying to create a Digital Terrain Model for Brasil. Publicly available sources are inadequate (SRTM has only 90m resolution (30m only for the US), ASTER has many artifacts, etc). So I intend to use crowsourced data from peoples GPSs...'''
date = "2014-01-22T13:20:00Z"
lastmod = "2014-02-04T09:19:00Z"
weight = 30075
keywords = [ "brazil", "accuracy", "elevation", "brasil", "gps" ]
aliases = [ "/questions/30075" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Extract Elevation from GPS tracks available in OSM](/questions/30075/extract-elevation-from-gps-tracks-available-in-osm)

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
<span id="post-30075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30075-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I intend to extract Elevation from GPS tracks available in OSM</p>
<p>I´m trying to create a Digital Terrain Model for Brasil. Publicly available sources are inadequate (SRTM has only 90m resolution (30m only for the US), ASTER has many artifacts, etc). So I intend to use crowsourced data from peoples GPSs and smartphones and do the patchwork myself.</p>
<p>I understand (from the links bellow) that OSM does not contain elevation data, and that elevation is not compatible with the data structure. Also that vertical precision (elevation) from GPSs is not very good (1.5 times horizontal precision, correct ? )</p>
<p>Some years GPS devices have barometers included. Since about 2012 higher end android smartphones also feature that. Is it possible to distinguish, in the GPS track "GPS elevation" from "barometer/altimeter" elevation?</p>
<p>regards Lucas</p>
<p><a href="https://help.openstreetmap.org/questions/999/how-to-extract-elevation-information-from-tracks-in-josm">https://help.openstreetmap.org/questions/999/how-to-extract-elevation-information-from-tracks-in-josm</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-brazil" rel="tag" title="see questions tagged &#39;brazil&#39;">brazil</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-brasil" rel="tag" title="see questions tagged &#39;brasil&#39;">brasil</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '14, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/120ccdbc8f99734785b77531756bb4cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LucasMation&#39;s gravatar image" />
<p><span>LucasMation</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LucasMation has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '14, 14:54</strong> </span></p>
</div>
</div>
<div id="comments-container-30075" class="comments-container">
<span id="30087"></span>
<div id="comment-30087" class="comment">
<div id="post-30087-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's worth looking at what Dan Stowell did using Gaussian processes with tagged ele=* values in the UK: <a href="http://www.mcld.co.uk/blog/">http://www.mcld.co.uk/blog/</a></p>
</div>
<div id="comment-30087-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 14:37)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30075-form-container" class="comment-form-container">
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

<span id="30082"></span>

<div id="answer-container-30082" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30082-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see here 2 questions mixed and will try to answer them one by one</p>
<ol>
<li><p><strong>GPS traces of OSM</strong><br />
They are available but contain only point cloud for privacy reasons: <a href="http://wiki.openstreetmap.org/wiki/Planet.gpx">http://wiki.openstreetmap.org/wiki/Planet.gpx</a><br />
Indeed you can crawl via the <a href="http://wiki.openstreetmap.org/wiki/API">OSM API</a> and scan and find if users have published raw traces in GPX format that might contain also ALT data. For example, I have some public traces: <a href="https://www.openstreetmap.org/user/!i!/traces/1112661">https://www.openstreetmap.org/user/!i!/traces/1112661</a></p></li>
<li><p><strong>DGM trough GPS 3D data</strong><br />
This is pretty hard for crowdsourcing as you say there are various different aspects that influence the quality. AFAIK neither GPX nor NMEA contain information about the Z-quality, but call me wrong.<br />
But there are some approaches to work on that topic as <a href="http://opendem.info">http://opendem.info</a> which seems now to put a focus esp. in barometric recordings (subsea height). Also <a href="http://wiki.openstreetmap.org/wiki/OSM2World">OSM2World</a> has some approaches to make use of OSM tagged height informations to improve the DEM shape locally, but AFAIK this is still WIP and not pushed in the mainline client.</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30082" class="comments-container">
<span id="30093"></span>
<div id="comment-30093" class="comment">
<div id="post-30093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you:</p>
<p>1)I agree. From your comment and the discussion above, it seems that it would be necessary to get the full Tracks and even some data from the html page with the link (to calibrate error as user fixed effects). I´m not a web programmer. Has anyone implemented such a crawler? Could I do that with "wget"? what would be the baseline url?</p>
<p>2) yes. But I imagine that some sort of statistical model can help solve, smooth the data, as indicated in the post above, (<a href="http://www.mcld.co.uk/blog/)">http://www.mcld.co.uk/blog/)</a></p>
</div>
<div id="comment-30093-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 15:56)</span> <span class="comment-user userinfo">LucasMation</span>
</div>
</div>
<span id="30106"></span>
<div id="comment-30106" class="comment">
<div id="post-30106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>to 1.) You can use e.g. scrapy to realize such an crawler easily. Please respect the terms of service and setup your service to do a min load. You might also consider to contact the <a href="https://wiki.osmfoundation.org/wiki/Data_Working_Group">OSMF data working group</a> maybe they can help you to get the GPX.</p>
<p>to 2.) I can just suggest recommend to talk to the <a href="http://wiki.openstreetmap.org/wiki/3D_Development">3D folks</a> as this is in general interest :)</p>
</div>
<div id="comment-30106-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:59)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-30082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30082-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30079"></span>

<div id="answer-container-30079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30079-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While you may find some devices where it is possible, I don't think you'll be able to see the physical data source in the generated gpx file.</p>
<p>For example on my altimeter-enhanced GPSMap62s, the altimeter and the gps are used as an aggregated sensor (one measure refining the other) and the output is a single value. There isn't even a UI to get the individual measurements. Same is true of combined GPS/GLONASS receivers : you get an enhanced but aggregate measurement.</p>
<p>That said, more and more devices store a DOP value in the gpx file. As long as it isn't stripped when uploaded to OSM, you can use that value as a (weak) hint of the measurement accuracy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30079" class="comments-container">
<span id="30085"></span>
<div id="comment-30085" class="comment">
<div id="post-30085-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want an example of a GPS trace in OSM with elavations from a barometric altimeter, there's one <a href="http://www.openstreetmap.org/user/SomeoneElse/traces/1644247">here</a>, from a Garmin eTrex Vista HCx. Nothing in there shouts out to me "these elevations are via a barometric altimeter". If you look at the numbers you'll see another problem - despite being calibrated to think that it was at 8m a couple of times during the day (the area of the trace is extremely flat) the recorded elevation drifted down consistently during the day.</p>
</div>
<div id="comment-30085-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 14:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30088"></span>
<div id="comment-30088" class="comment">
<div id="post-30088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting. Does the data contain metadata (or some field) on the device manufacturer and model? Maybe knowing this I could map which devices use barometer. What do you think?</p>
<p>Bare in mind that the alternative is using SRTM satellite data, with 90m pixel, and vertical accuracy of 7-14m for 1sd (68%) or +o-45m if you want a 99% confidence interval</p>
</div>
<div id="comment-30088-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 14:40)</span> <span class="comment-user userinfo">LucasMation</span>
</div>
</div>
<span id="30096"></span>
<div id="comment-30096" class="comment">
<div id="post-30096-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You'd need to compare the contents of a public trace from a non-barometric altimeter eTrex with the one that I linked to. Maybe ask in #osm on IRC to see if anyone can quickly point to one?</p>
</div>
<div id="comment-30096-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30079-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30414"></span>

<div id="answer-container-30414" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Update and further questions:</p>
<p>1)Following the suggestions above, I built the web scrapper (programmed it in Stata a statistical package whose programming language I´m familiar with). It works like this:</p>
<p>a)run a loop through every "menu pape" (like this page: <a href="http://www.openstreetmap.org/traces/page/1)">http://www.openstreetmap.org/traces/page/1)</a> parsing the HTML to extract information (url, contributor name and date) of each fo the 20 tracks per page. There are about 47000 menu pages. Joining the info on all "menu pages" I have a list of the URLs for each track (like this: <a href="http://www.openstreetmap.org/user/kwiky/traces/1651084)">http://www.openstreetmap.org/user/kwiky/traces/1651084)</a> and also the URL to download the file.</p>
<p>b) For each track in the list created above, visit the specific ulr and extract the initial coordinate.</p>
<p>c) If that coordinate falls within Brazil, download the data.</p>
<p>I think I got it to work, but OSM server seems to be cutting me off "a)", after about 500 or so "menu pages" scrapped. Does any one know what is happening? I tried slowing the process down, making the computer stop for 2 seconds after scrapping every page but that did not work either.</p>
<p>2) I just googled again now and found this post: <a href="http://blog.osmfoundation.org/2013/04/12/bulk-gpx-track-data/">http://blog.osmfoundation.org/2013/04/12/bulk-gpx-track-data/</a> claiming that you can get the full gpx files, available from here: <a href="http://planet.osm.org/gps/">http://planet.osm.org/gps/</a> has anyone used this data? Also, is it available/duplicated elsewhere for download? The file is 21GB and the download is super slow (my connection here is pretty fast). It computer is predictin it will take 17 days to download.</p>
<p>again, any help on this would be appreciated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '14, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/120ccdbc8f99734785b77531756bb4cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LucasMation&#39;s gravatar image" />
<p><span>LucasMation</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LucasMation has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30414" class="comments-container">
<span id="30415"></span>
<div id="comment-30415" class="comment">
<div id="post-30415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you should use the "edit" link below your question and add the text there. This is no discusion forum here. Maybe that would be the better way anyway...</p>
</div>
<div id="comment-30415-info" class="comment-info">
<span class="comment-age">(03 Feb '14, 18:20)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30416"></span>
<div id="comment-30416" class="comment">
<div id="post-30416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re "getting cut off" I'd be tempted to ask on <a href="http://wiki.openstreetmap.org/wiki/Irc">IRC in #osm-dev</a>. Re the usefulness or otherwise of <a href="http://planet.osm.org/gps/">http://planet.osm.org/gps/</a>, <a href="http://wiki.openstreetmap.org/wiki/Planet.gpx">this page</a> suggests it's just lat and long, so probably not helpful to you.</p>
</div>
<div id="comment-30416-info" class="comment-info">
<span class="comment-age">(03 Feb '14, 19:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30430"></span>
<div id="comment-30430" class="comment">
<div id="post-30430-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, see link in my post, this is just a simple 2D pointcloud</p>
</div>
<div id="comment-30430-info" class="comment-info">
<span class="comment-age">(04 Feb '14, 09:19)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-30414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30414-form-container" class="comment-form-container">
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


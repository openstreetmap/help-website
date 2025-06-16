+++
type = "question"
title = "incorrect geocoding result"
description = '''Hello. I&#x27;m new to here. I&#x27;ve set up my own Nominatim server on a Ubuntu server and imported the full planet OSM file into the database. Map rendering is fine, however, the reverse geocoding result was very strange, in some cases the result returned from my local server is different to the Nominatim ...'''
date = "2013-05-04T16:21:00Z"
lastmod = "2013-05-04T18:07:00Z"
weight = 22093
keywords = [ "incorrect", "geocoding", "result" ]
aliases = [ "/questions/22093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [incorrect geocoding result](/questions/22093/incorrect-geocoding-result)

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
<span id="post-22093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22093-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I'm new to here.</p>
<p>I've set up my own Nominatim server on a Ubuntu server and imported the full planet OSM file into the database. Map rendering is fine, however, the reverse geocoding result was very strange, in some cases the result returned from my local server is different to the Nominatim webpage. Of course, the result from Nominatim is correct.</p>
<p><strong>For example:</strong> <em><u><a href="http://MY_SERVER/nominatim/reverse?format=xml&amp;lat=22.300348&amp;lon=114.167846&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en">http://MY_SERVER/nominatim/reverse?format=xml&amp;lat=22.300348&amp;lon=114.167846&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en</a></u></em></p>
<p><br />
<strong>My server returns:</strong> &lt;reversegeocode timestamp="Sat, 04 May 13 14:42:00 +0000" attribution="Data © OpenStreetMap contributors, ODbL 1.0. &amp;lt;a href=" http:="" www.openstreetmap.org="" copyright""=""&gt;https://www.openstreetmap.org/copyright" querystring="format=xml&amp;lat=22.300348&amp;lon=114.167846&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en"&gt; &lt;result place_id="12826225" osm_type="node" osm_id="1187352818" ref="China Hong Kong City" lat="22.3009605" lon="114.1676224"&gt; China Hong Kong City, Canton Road, Tsim Sha Tsui, Yau Tsim Mong District, <strong>New Territories</strong>, Hong Kong &lt;/result&gt; &lt;addressparts&gt; &lt;parking&gt;China Hong Kong City&lt;/parking&gt; &lt;road&gt;Canton Road&lt;/road&gt; &lt;suburb&gt;Tsim Sha Tsui&lt;/suburb&gt; &lt;city&gt;Yau Tsim Mong District&lt;/city&gt; &lt;county&gt;<strong>New Territories</strong>&lt;/county&gt; &lt;state&gt;Hong Kong&lt;/state&gt; &lt;country&gt;Hong Kong&lt;/country&gt; &lt;country_code&gt;hk&lt;/country_code&gt; &lt;/addressparts&gt; &lt;/reversegeocode&gt;</p>
<p><strong>The Nominatim server returns:</strong> &lt;reversegeocode timestamp="Sat, 04 May 13 14:42:08 +0000" attribution="Data © OpenStreetMap contributors, ODbL 1.0. &amp;lt;a href=" http:="" www.openstreetmap.org="" copyright""=""&gt;https://www.openstreetmap.org/copyright" querystring="format=xml&amp;lat=22.300348&amp;lon=114.167846&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en"&gt; &lt;result place_id="12824996" osm_type="node" osm_id="1187352818" ref="China Hong Kong City" lat="22.3009605" lon="114.1676224"&gt; China Hong Kong City, Canton Road, Tsim Sha Tsui, Yau Tsim Mong District, <strong>Kowloon</strong>, Hong Kong &lt;/result&gt; &lt;addressparts&gt; &lt;parking&gt;China Hong Kong City&lt;/parking&gt; &lt;road&gt;Canton Road&lt;/road&gt; &lt;suburb&gt;Tsim Sha Tsui&lt;/suburb&gt; &lt;city&gt;Yau Tsim Mong District&lt;/city&gt; &lt;county&gt;<strong>Kowloon</strong>&lt;/county&gt; &lt;state&gt;Hong Kong&lt;/state&gt; &lt;country&gt;Hong Kong&lt;/country&gt; &lt;country_code&gt;hk&lt;/country_code&gt; &lt;/addressparts&gt; &lt;/reversegeocode&gt;<br />
The COUNTY value is different and "Kowloon" is the correct one.</p>
<p>I tried to import it from OSM/PBF file, the results are same.</p>
<p>I strictly went through the installation procedure (<a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation)">https://wiki.openstreetmap.org/wiki/Nominatim/Installation)</a> and tried to install it with Nominatim 2.0.1 and the GIT version, results are still same...</p>
<p>Is there anyone have any idea about this? If anyone is able to help me troubleshoot, I can give you root access to my server.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-result" rel="tag" title="see questions tagged &#39;result&#39;">result</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '13, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/e1d21bf0156f12ba67fcb192c5667790?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sa9496&#39;s gravatar image" />
<p><span>sa9496</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sa9496 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-22093" class="comments-container">
<span id="22098"></span>
<div id="comment-22098" class="comment">
<div id="post-22098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh yes.. I found the New Territories boundary is different:</p>
<p>My server: <a href="http://54.225.111.130/nominatim/details.php?place_id=113082147">http://54.225.111.130/nominatim/details.php?place_id=113082147</a><br />
Nominatim: <a href="http://nominatim.openstreetmap.org/details.php?place_id=98186275">http://nominatim.openstreetmap.org/details.php?place_id=98186275</a><br />
</p>
<p>Does it actually mean that my data is older than what Nominatim is using? Mine was dated 2013-04-23 (few days before I downloaded the planet file) and the Nominatim one was 2013-05-04 (today)</p>
<p>Do you think I can have it fixed if I update my database?</p>
</div>
<div id="comment-22098-info" class="comment-info">
<span class="comment-age">(04 May '13, 18:07)</span> <span class="comment-user userinfo">sa9496</span>
</div>
</div>
</div>
<div id="comment-tools-22093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22093-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="22095"></span>

<div id="answer-container-22095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22095-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a data problem: I suspect that your version of the planet is newer than that used by Nominatim (at least for Kowloon).</p>
<p>It is always worth using the detail view of Nominatim to see what it thinks the boundaries of polygons actually are. The current boundaries for Kowloon and <a href="http://nominatim.openstreetmap.org/search.php?q=New+Territories">New Territories</a> are <a href="http://nominatim.openstreetmap.org/details.php?place_id=98217453">here</a> and <a href="http://nominatim.openstreetmap.org/details.php?place_id=98186275">here</a> (as these use internal Nominatim Ids, these links may fail in which case chose the links on the name and select the details link in Nominatim). You should check that the boundaries for these places are the same on your server.</p>
<p>In fact the boundary of Kowloon was has been changed in several changesets recently - see the history of the relation <a href="https://www.openstreetmap.org/browse/relation/2279652/history">here</a> - and it is no longer a closed polygon as shown by inspecting the relation <a href="http://analyser.openstreetmap.fr/cgi-bin/index.py">here</a>.</p>
<p>In addition the relation covering the <a href="https://www.openstreetmap.org/browse/relation/2279783">New Territories</a> has similarly lost its hole containing Hong Kong Island and Kowloon.</p>
<p>Once these problems have been fixed and your Nominatim instance updated I would expect that you will get the geocoding results you expect!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '13, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-22095" class="comments-container">
<span id="22096"></span>
<div id="comment-22096" class="comment">
<div id="post-22096-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have now fixed the admin polygons for Kowloon, Hong Kong Island and New Territories which had been broken.</p>
</div>
<div id="comment-22096-info" class="comment-info">
<span class="comment-age">(04 May '13, 17:27)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22095-form-container" class="comment-form-container">
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


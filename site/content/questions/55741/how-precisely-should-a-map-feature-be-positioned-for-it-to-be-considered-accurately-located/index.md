+++
type = "question"
title = "How precisely should a map feature be positioned for it to be considered accurately located?"
description = '''I am trying to work out how precise I should be when positioning features in OSM. Of the questions already asked, &quot;Aligning roads to proper locations&quot; perhaps comes closest to what I am asking about, but doesn&#x27;t really answer my question. After taking several of my GPS traces and averaging them, as ...'''
date = "2017-04-22T04:31:00Z"
lastmod = "2020-07-09T08:26:00Z"
weight = 55741
keywords = [ "imagery", "position", "gps", "precision", "accuracy" ]
aliases = [ "/questions/55741" ]
osqa_answers = 7
osqa_accepted = true
+++

<div class="headNormal">

# [How precisely should a map feature be positioned for it to be considered accurately located?](/questions/55741/how-precisely-should-a-map-feature-be-positioned-for-it-to-be-considered-accurately-located)

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
<span id="post-55741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55741-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-55741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to work out how precise I should be when positioning features in OSM. Of the questions already asked, "<a href="https://help.openstreetmap.org/questions/17661/aligning-roads-to-proper-location">Aligning roads to proper locations</a>" perhaps comes closest to what I am asking about, but doesn't really answer my question. After taking several of my GPS traces and averaging them, as well as aligning the aerial imagery with them, and then drawing various map features, such as buildings and fences, I still find a discrepancy when I go and compare OSM with other sources of supposedly "accurate" geographic information.</p>
<p>For example: the <a href="http://data.linz.govt.nz/data/">LINZ Data Service</a> has an OSM base map that allows one to display a wide range of aerial photographs, GIS and cadstral mapping layers from LINZ data over the top of OSM. As far as I can tell the LINZ data uses current or near current OSM data. In some cases I have been able to closely align various map features with the corresponding LINZ information, so that they overlay each other very closely.</p>
<p>What I want to know is how close to the real world should I attempt to plot various map features, given all the uncertainties involved. Although the OSM database can record nodes to the nearest centimetre, or so, I realise that such a level of precision is probably not going to be practically achievable most of the time. But what level of precision should I consider is sufficient for an accurate OSM?</p>
<p>That is, how precise should I try to be?</p>
<p>And at what point should I stop worrying about precise positioning because the uncertainties become too great and so make further precision meaningless.</p>
<p>For example: In Potlatch 2's wireframe mode at zoom level 19, the black wireframe lines would seem to be about 0.1 metres wide and nodes about 0.5 to 1 metre square. However, most of the time my GPS data is rarely more accurate than 3 metres and the position wanders around while the GPS unit is stationary. When I average my GPS data by taking several samples over time, I can only get the precise position to within about a metre or so. At zoom level 19, after aligning the imagery and my GPS traces, I find there is still a positional uncertainty of about 1 to 3 metres.</p>
<p>Is a positional uncertainty of +/- 3 metres sufficiently precise for OSM? (At least at zoom level 19 or less.)</p>
<p>And how positionally precise should I attempt to be at various other zoom levels? For example: Should I try to be precise to 1 cm at the highest zoom level of 23, say?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-position" rel="tag" title="see questions tagged &#39;position&#39;">position</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span> <span class="post-tag tag-link-precision" rel="tag" title="see questions tagged &#39;precision&#39;">precision</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '17, 04:31</strong></p>
<img src="https://secure.gravatar.com/avatar/1a623cf4b5df74bee1b91d0c21736921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Huttite&#39;s gravatar image" />
<p><span>Huttite</span><br />
<span class="score" title="560 reputation points">560</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Huttite has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55741" class="comments-container">
&#10;</div>
<div id="comment-tools-55741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55741-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="55957"></span>

<div id="answer-container-55957" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55957-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-55957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Huttite has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I live in an area that was quite active early on in OSMs history. At the time, with the exception of some rather off yahoo imagery for some areas, the only way to contribute was via generating GPS tracks and naturally that meant over- and under-runs in corners by 2 digit numbers of meters, wrong topology (roads merging in to the wrong one in a complicated junction for example) and in places where reception in general is not so good (forests etc) way off tracks, but the result was perfectly usable (actually the topology issues were and are far more annoying than anything else).</p>
<p>As I mentioned we had some coverage by yahoo imagery early on and in those areas we've spent the last couple of years cleaning up details (mainly buildings) that were added from that imagery but unluckily from a bad source, creating a lot of completely unnecessary work with no real benefit at the time.</p>
<p>As a consequence, getting back to answering the question. I believe the correct answer is that the required precision depends on the level of detail you want to add and as a corollary you shouldn't be adding detail where the available sources do not support that level of precision reasonably.</p>
<p>Example: if you only have consumer grade GPS and no imagery, I would restrict myself to roads and map POIs as nodes and not try to add buildings en masse.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '17, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '17, 12:14</strong> </span></p>
</div>
</div>
<div id="comments-container-55957" class="comments-container">
<span id="56005"></span>
<div id="comment-56005" class="comment">
<div id="post-56005-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks Simon. Your answer contains the sort of information I was wanting to obtain.</p>
<p>First and foremost is map topology, i.e. connecting streets so the street centre-line network has the correct shape and positioning points of interest in the right order, with respect to the street network.</p>
<p>Then comes the detail, but only sufficient detail that can be supported by the available GPS data and any available imagery.</p>
<p>Getting the street network reasonably aligned with imagery and GPS data should give clues about how accurate one can be. Additional external sources, such as official cadastral data, will help judging how accurate OSM is, and suggest how accurate one can be.</p>
<p>(e.g. In NZ, OSM is a background layer for official LINZ (cadastral) data.)</p>
<p>Buildings and other details should be added last, once one has good quality imagery available to trace and one is confident it is precisely positioned with respect to the street network. Draw in significant and notable buildings first but do not add all the buildings unless there is good quality imagery available.</p>
</div>
<div id="comment-56005-info" class="comment-info">
<span class="comment-age">(03 May '17, 09:34)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
</div>
<div id="comment-tools-55957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55957-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55749"></span>

<div id="answer-container-55749" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55749-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-55749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the answer is probably to decide for yourself what level of accuracy improves the overall data the most. Working to add centimeter precision buildings is often going to be less useful than adding rough alignments for missing roads or correcting larger issues with roads. An address point probably provides users with more eventual value than a building outline of any precision. And so on.</p>
<p>I think it is still worthwhile to pay attention to what sort of accuracy and precision you get out of your mapping process and to look for improvements, I just don't think it is the thing with the highest priority.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '17, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55749" class="comments-container">
<span id="55781"></span>
<div id="comment-55781" class="comment">
<div id="post-55781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My question is not about the accuracy of the map but about its precision. Assuming I have added those missing roads and buildings so that they are accurately represented, but perhaps imprecisely positioned, and so may want to make adjustments. At what degree of precision should I say the extra effort is not worthwhile. While I might know the dimensions of a particular building and other features on a particular property to the nearest centimetre, because I have a site survey, I don't know the exact position or location because the aerial imagery is offset and my GPS measurements are only precise to +/- 1 to 3 metres (I hope). And the two do not align perfectly. Also, I don't know for certain which one is "out" and suspect they both could be. What I am trying to ascertain is what is an acceptable degree of precision. I realise +/- 1 centimete is too precice but is +/- 3 metres precise enough? Such a degree of precision could mean the difference between walking along a fence or in the gutter rather than the middle of a footpath. Is that acceptable with typical handheld GPS technology and the existing Bing imagery?</p>
</div>
<div id="comment-55781-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 00:58)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
<span id="55784"></span>
<div id="comment-55784" class="comment">
<div id="post-55784-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, a few meters is fine. Lots of people are adding lots of features without thinking much about how good the source is, so there is a bit of a baseline.</p>
</div>
<div id="comment-55784-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 01:29)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="55790"></span>
<div id="comment-55790" class="comment">
<div id="post-55790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you be more precise about "a few metres"? Do you mean something in the range of 1 to 5 metres, say, or is it more like 10 to 30 metres? In other words, is it the width of a footpath (~ 1 to 3 m), a traffic lane(~ 4 to 5 m), a street or road (~7 to 10 m), or a property frontage (~ 20 to 30 m) for example.</p>
</div>
<div id="comment-55790-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 05:28)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
<span id="55827"></span>
<div id="comment-55827" class="comment">
<div id="post-55827-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It really depends. I wouldn't map buildings that I thought were 15 meters off, but I wouldn't hesitate to add a section of hiking trail that was 30 meters off (I would try to do better, but noting the approximate route of the trail is better than leaving it out). Same thing with a road, even if the best source isn't great, I still think it is better to have something than nothing.</p>
</div>
<div id="comment-55827-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 16:15)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="56008"></span>
<div id="comment-56008" class="comment">
<div id="post-56008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I question the "something is better than nothing" approach with roads and trails. Even if a road or trail cannot be precisely positioned on the map, it should at least be accurately represented.</p>
<p>I recently encountered a street that was perhaps drawn 30 metres out of position. However it showed that one entered from the top of the street rather than the bottom. As a consequence, if one tried to follow the map, one found the street went up a flight of steps and then down a private footpath, rather than climbing along the rising edge of a vertical cliff then turning hard back in a zig-zag turn to go up the rest of the street. Because the cliff edge had given way, one could not drive up the road safely. However, pedestrians could walk up the steps and along the footpath to access the top end of the street. The inaccurate map meant you couldn't drive to where the map said you could but if you followed the street signs, and just thought the map showed the road out of position, you could end up driving over the cliff edge.</p>
<p>When I looked at the imagery I wondered how anyone could make such a mistake, because the road was clearly shown. but the steps were not visible.</p>
</div>
<div id="comment-56008-info" class="comment-info">
<span class="comment-age">(03 May '17, 10:45)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
</div>
<div id="comment-tools-55749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55749-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55744"></span>

<div id="answer-container-55744" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55744-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Huttile, it all comes down on the accuracy of your own GPS. If its +- 3.00 m you won’t be able to beat that figure. A professional GPS does it better, you don’t wont to carry it around, is accurate up to 0,01 m. OSM is based on the availability of many trails or tracks of a way, the truth will statistically be somewhere in the middle. When I survey a specific building, I draw it outside the map locally using JOSM and based on the original building drawings (4 hours work), if available and place the figure inside the GPS nodes or marks, just to reduce the variations of the GPS traces.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '17, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-55744" class="comments-container">
<span id="55782"></span>
<div id="comment-55782" class="comment">
<div id="post-55782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think it does just come down to the "accuracy" - really its the precision - of my own GPS. I know my GPS traces are only accurate to about +/- 3 metres and I know they change from moment to moment, so I know I need to use multiple traces or take fixes for "averaged waypoints". Even when I plot these points, precisely, I still notice that there are small discrepancies between my GPS and Bing imagery, for example. And I cannot tell if either are more precise! You seem to be suggesting that I should not be too concerned if things are mapped to within +/- 3 metres, since obtaining better precision requires using professional surveying equipment and techniques.</p>
</div>
<div id="comment-55782-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 01:14)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
<span id="55810"></span>
<div id="comment-55810" class="comment">
<div id="post-55810-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think you should not be too concerned if it prevents you from doing other mapping work for example.</p>
<p>The precision will increase in a few years with Galileo and the GPS III update so it'll be much easier to map down to 1 meter.</p>
<p>In the mean time, both mappers and users will have a much lower precision, up to 3 meters for the maps + up to 3 meters for the user's GPS, so up to 6 meters on the map.</p>
</div>
<div id="comment-55810-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 13:44)</span> <span class="comment-user userinfo">The RedBurn</span>
</div>
</div>
</div>
<div id="comment-tools-55744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55744-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55752"></span>

<div id="answer-container-55752" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55752-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just would like to add that I often find it useful if mappers document their position sources. It helps other mappers later on (or even the original mapper themselves) to judge about an objects positional accuracy. For example if a mapper documented (in a changeset <code>comment</code>/<code>source</code> or possibly even in a <code>source:position</code> tag on an object) that the position of a (for example) tower was acquired with averaging 10 EGNOS-DGPS-assisted GPS measurements over different days, then I would not want to move a point based on my single-pass GPS measurement or nowadays aerial imagery.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '17, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55752" class="comments-container">
<span id="55785"></span>
<div id="comment-55785" class="comment">
<div id="post-55785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Definitely agree. In areas where I am mapping I have often selected feature visible in the imagery that I can use as a GPS waypoint position. Features like the end posts of a fence or similar barrier, or foot of a power pole that show as a clear sharp feature, with a linear shadow are good candidates.</p>
<p>The problem arises when I have several of these points but cannot get them all to align precisely with the imagery, so have to compromises with using a close fit when a couple of reasonably close points are "out" by a metre or two over about 50 metres distance. I am assuming that even my "averaged waypoints" could be uncertain by 1 or 2 metres, because they seem to move around by that much each time I take another sample. Is this degree of imprecision acceptable for OSM, given the current state of GPS technology and Bing imagery? Or am I being too precise? Should I tolerate and accept more error in my measurements?</p>
</div>
<div id="comment-55785-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 01:41)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
<span id="55787"></span>
<div id="comment-55787" class="comment">
<div id="post-55787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you shouldn't be to focussed on aligning with Bing. I believe Bing is never very precise, the position of a feature can vary depending on the zoom level, stitching can be done badly, etc.</p>
</div>
<div id="comment-55787-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 04:06)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="55788"></span>
<div id="comment-55788" class="comment">
<div id="post-55788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am very aware that Bing imagery is not precisely positioned. I often find I have to adjust the offset of the original image by 10 or 20 metres so that it aligns with a particular part of the map. Yes, there are places where the different image boundaries are poorly stitched together but these are fairly obvious distortions over a small area or strip of image. Also I have found some places where the ortho-rectification process seems questionable, particularly near high cliffs or steep hills. However, once I align the imagery reasonably precisely, I do find it is remains fairly accurately aligned with features that are hundreds of metres or even kilometres apart. Perhaps just needing a tweek of a metre or so as I move a thousand metres from one reference point to the next.</p>
<p>While I might take care to align the imagery with points I believe are precisely located, it is readily apparent that others might not take quite the same care. Often I encounter places where an area has been mapped directly off the imagery without it being aligned to precisely known locations. How much "misalignment" should I tolerate before moving whole city blocks of the map just a few metres sideways?</p>
</div>
<div id="comment-55788-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 05:14)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
<span id="55833"></span>
<div id="comment-55833" class="comment">
<div id="post-55833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11060/huttite"></a><a href="https://help.openstreetmap.org/users/11060/huttite">@Huttite</a>: in any way you should be sure that your alignment really is better than before. Maybe also contact the former (main) mappers if they are still active and/or shortly discuss on a (preferably) local mailinglist or forum. I would move whole blocks if their absolute mispositioning becomes a problem. E.g. if building corners (old position) intrude street or park areas (new, good position). That likely is something around 5 m - depending on the city type.</p>
</div>
<div id="comment-55833-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 19:54)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55752-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55954"></span>

<div id="answer-container-55954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55954-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An important question in this context is "how precise/accurate do we really need to be in order to produce a map that is useful for most users?".</p>
<p>One thing is going OCD about "how accurate/precise can we possibly be with the tools at our hands", another thing is asking "how accurate/precise do most users really need the map to be?".</p>
<p>Imagine a user riding a car or a bicycle; What's the chance that he would notice if a building or sign or whatever on the map was 3-5 meters off? My personal experience = really slim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '17, 07:06</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55954" class="comments-container">
<span id="55959"></span>
<div id="comment-55959" class="comment">
<div id="post-55959-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>could you please un-abbreviate "OCD"? I fail to understand its meaning.</p>
</div>
<div id="comment-55959-info" class="comment-info">
<span class="comment-age">(29 Apr '17, 11:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="55961"></span>
<div id="comment-55961" class="comment">
<div id="post-55961-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://en.wikipedia.org/wiki/Obsessive%E2%80%93compulsive_disorder">https://en.wikipedia.org/wiki/Obsessive%E2%80%93compulsive_disorder</a></p>
</div>
<div id="comment-55961-info" class="comment-info">
<span class="comment-age">(29 Apr '17, 16:43)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="56007"></span>
<div id="comment-56007" class="comment">
<div id="post-56007-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I was walking I might notice that a path was 5 metres off if it was a good GPS day, but in a car or on a bicycle it would be less noticeable on a single occasion. However, repeated passes on different days could show up an error. However, as you say, is a map being that precise really needed by most users? Probably not needed if you are trying to find a public road. But it might be if the map is used as a background image for displaying official GIS data, which it is for Land Information in NZ (LINZ data) and Geonet.org.nz, for example. While locating the epicentre of an earthquake to the nearest kilometre is good enough, you may want to locate the centreline of a road or a boundary fence within a metre or so.</p>
</div>
<div id="comment-56007-info" class="comment-info">
<span class="comment-age">(03 May '17, 10:11)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
<span id="56009"></span>
<div id="comment-56009" class="comment">
<div id="post-56009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>TL;DR: As precise as needed, but not more ;)</p>
<p>In my humble opinion, much of OSM use is by humans; so I'm mapping on a human scale: within a few meters (~20 feet?). If it does matter topologically (multiple footpaths in an urban terrain), I try to be more precise, but I don't think the data is actually usable for precision under 1 m (~3 ft) - the precision of individual points is, IMNSHO, unknown.</p>
</div>
<div id="comment-56009-info" class="comment-info">
<span class="comment-age">(03 May '17, 11:42)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="56062"></span>
<div id="comment-56062" class="comment">
<div id="post-56062-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In other words, having the road centreline plotted on the carriageway between the property boundary fences is sufficient precision for human uses, but the data won't support putting the centreline on top of the 10 cm (4 inch) white line in the middle of the road. Although, if you tried to be really precise you could try and draw a road centreline in the middle of a road in the gap between traffic travelling in opposite directions.</p>
<p>I.e You can find the road to travel on it, but you shouldn't be using OSM to find a buried pipe or power cable shown to be in the street.</p>
</div>
<div id="comment-56062-info" class="comment-info">
<span class="comment-age">(06 May '17, 03:14)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
</div>
<div id="comment-tools-55954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55954-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59797"></span>

<div id="answer-container-59797" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59797-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>After taking several of my GPS traces and averaging them, as well as aligning the aerial imagery with them, and then drawing various map features, such as buildings and fences, I still find a discrepancy when I go and compare OSM with other sources of supposedly "accurate" geographic information.</p>
</blockquote>
<p>if you have accurate geographic information (building positions, survey points, survey maps from national geodetic service) then you should use those, provided the copyright allows for that. Important part is that you need to make sure you use the same reference frame or convert to the one OSM uses: WGS 84.</p>
<blockquote>
<p>What I want to know is how close to the real world should I attempt to plot various map features, given all the uncertainties involved. Although the OSM database can record nodes to the nearest centimetre, or so, I realise that such a level of precision is probably not going to be practically achievable most of the time. But what level of precision should I consider is sufficient for an accurate OSM?</p>
<p>That is, how precise should I try to be?</p>
</blockquote>
<p>Here again the problem is that OSM uses WGS 84. Problem with WGS 84 is that it does not account for continental drift and plate movement (that's one of the reasons why national bodies use their own reference frames). So for <em>absolute</em> positioning the best you can do is around 10 to 20 cm. More precise measurements will quickly get invalidated by natural processes.</p>
<p>Given that the smallest items we do map (waste baskets, road signs, kerbs, etc.) are also 10 to 20 cm, a 1 cm level of precision, even in relative measurement, I'd say is overkill. For relative measurement, more important is information about the side of the path the bin is (or the side of a road the walkway is on), than the length away it is from the nearest junction.</p>
<p>Similarly, for navigation for blind people, it's more important that you have a waste basket in front of bench than absolutely precise position of the waste basket but incorrect relative position of the bench near it.</p>
<blockquote>
<p>Is a positional uncertainty of +/- 3 metres sufficiently precise for OSM? (At least at zoom level 19 or less.)</p>
</blockquote>
<p>in the middle of nowhere, any data is better than no data - information that there is a road that leads from mapped point A to mapped point B and the general shape of it is useful (remember, you do not have to even use GPS or aerial maps for mapping in OSM!). Still, good practice in such situation is to either add <code>fixme=resurvey</code> tag, or <code>source=approximation</code> to the changeset. Similarly, if the best measurement you have is regular aerial imaginary (Bing, Yahoo) and GPS trace, then adding <code>source=gps</code> is good practice.</p>
<p>If you do have access to ortophotographs, then I'd say you should map buildings and roads to within a meter or few decimeters (unless the photo has a lower resolution than that).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '17, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7cfe49e263a76df97bd6defdb1a86714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomato42&#39;s gravatar image" />
<p><span>tomato42</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomato42 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59797" class="comments-container">
&#10;</div>
<div id="comment-tools-59797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59797-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75612"></span>

<div id="answer-container-75612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75612-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-75612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for sharing about how precisely should a map feature be positioned for it to be considered accurately located, your information helpful for all peoples. I am also working on a project for indoor positioning.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '20, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75612" class="comments-container">
&#10;</div>
<div id="comment-tools-75612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75612-form-container" class="comment-form-container">
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


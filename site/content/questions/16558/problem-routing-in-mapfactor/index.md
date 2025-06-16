+++
type = "question"
title = "problem routing in mapfactor."
description = '''Hi all. In my city, trying to set route to navigate, strangely mapfactor navigator free (wich uses openstreetmap for its maps) traced every time an &quot;illogical&quot; route. It is a very heavy traffic load at this point. For saying something to reach a city that is 30 km away from mine, in a practically re...'''
date = "2012-10-01T01:52:00Z"
lastmod = "2012-10-01T23:02:00Z"
weight = 16558
keywords = [ "broken", "route" ]
aliases = [ "/questions/16558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [problem routing in mapfactor.](/questions/16558/problem-routing-in-mapfactor)

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
<span id="post-16558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16558-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all.</p>
<p>In my city, trying to set route to navigate, strangely mapfactor navigator free (wich uses openstreetmap for its maps) traced every time an "illogical" route. It is a very heavy traffic load at this point. For saying something to reach a city that is 30 km away from mine, in a practically rect line over one route, navigator traced to make 150 km, and take many other routes.</p>
<p>Today i decided to find (or try) what was going on, and i believe i found it. But i wanted to ask to you if this could solve de problem. In the picture below, openstreetmap show a "discontinued" route in that segment. Could this makes all the "illogical" routing?</p>
<p>I have already asked to mapfactor forums and i am waiting for answer. But i thougth to ask you too ;-)</p>
<p>Anyway i fixed it in the map, because it's not a broken route.</p>
<p><img src="http://svarez.com.ar/ruta22-cortada.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-broken" rel="tag" title="see questions tagged &#39;broken&#39;">broken</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '12, 01:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d9f0a950ef2392c34c847a1444953507?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juan%20Facundo&#39;s gravatar image" />
<p><span>Juan Facundo</span><br />
<span class="score" title="86 reputation points">86</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juan Facundo has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-16558" class="comments-container">
<span id="16570"></span>
<div id="comment-16570" class="comment">
<div id="post-16570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>by the way, an error near about mentioned above:</p>
<p>This highway intersects the highway #182797204 but there is no junction node. The picture:</p>
<p><img src="http://svarez.com.ar/error-01.png" alt="alt text" /></p>
<p>How can i fix this? because the bridge crosses OVER the other route. Just ignore the error? or is there another way?</p>
</div>
<div id="comment-16570-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 11:50)</span> <span class="comment-user userinfo">Juan Facundo</span>
</div>
</div>
<span id="16572"></span>
<div id="comment-16572" class="comment">
<div id="post-16572-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In order to make it clear that the road on the bridge doesn't join the road underneath, add the <a href="https://wiki.openstreetmap.org/wiki/Layer">layer</a> tag. Items with a larger layer number are above items with a lower layer number. In this case adding layer=1 to the bridge will make it clear that it goes over the road (items without a layer tag are assumed to be layer=0).</p>
</div>
<div id="comment-16572-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 12:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16573"></span>
<div id="comment-16573" class="comment">
<div id="post-16573-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please create a separate question next time. The <a href="https://www.openstreetmap.org/browse/way/182428667">highway</a> has a <em>bridge</em> tag, but misses the <em><a href="https://wiki.openstreetmap.org/wiki/Key:layer">layer</a></em> tag. You should add this tag (<em>layer=1</em> in this specific case) whenever two highways intersect - additionally to the <em>bridge</em> or <em>tunnel</em> tag.</p>
</div>
<div id="comment-16573-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 12:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="16574"></span>
<div id="comment-16574" class="comment">
<div id="post-16574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again and sorry for not creating a new question. It was a mistake.</p>
</div>
<div id="comment-16574-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 12:07)</span> <span class="comment-user userinfo">Juan Facundo</span>
</div>
</div>
</div>
<div id="comment-tools-16558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16558-form-container" class="comment-form-container">
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

<span id="16560"></span>

<div id="answer-container-16560" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16560-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, routers won't route over discontinued roads or missing road junctions. These are common errors for beginners and should be fixed, <a href="http://keepright.ipax.at/report_map.php?zoom=13&amp;lat=-38.95806&amp;lon=-68.27981&amp;layers=B0T&amp;ch=0%2C30%2C40%2C50%2C70%2C90%2C100%2C110%2C120%2C130%2C150%2C160%2C180%2C191%2C192%2C193%2C194%2C195%2C196%2C197%2C198%2C201%2C202%2C203%2C204%2C205%2C206%2C207%2C208%2C210%2C220%2C231%2C232%2C270%2C281%2C282%2C283%2C284%2C285%2C291%2C292%2C293%2C294%2C311%2C312%2C313%2C320%2C350%2C370%2C380%2C401%2C402%2C411%2C412%2C413&amp;show_ign=1&amp;show_tmpign=1">Keep Right</a> will help you with that. It shows several other similar errors in your area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '12, 06:15</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-16560" class="comments-container">
<span id="16564"></span>
<div id="comment-16564" class="comment">
<div id="post-16564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi skai, can i use this "keep right" to find errors in my place? how do i use it exactly? thanks</p>
</div>
<div id="comment-16564-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 08:58)</span> <span class="comment-user userinfo">JCsM</span>
</div>
</div>
<span id="16566"></span>
<div id="comment-16566" class="comment">
<div id="post-16566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>go to <a href="http://keepright.at">http://keepright.at</a> ... choose the right continent for your purposes, and then zoom to your area to see any errors or not.</p>
</div>
<div id="comment-16566-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 09:09)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="16567"></span>
<div id="comment-16567" class="comment">
<div id="post-16567-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@JCsM</span> Of course you can. Just move to your area and click on one of the bolt symbols, a popup should open explaining the error. There you can also directly open the corresponding area in Potlatch or JOSM to fix it. Afterwards you should mark the error as corrected in the popup so that other users don't try to fix it again.</p>
<p>There is also a <a href="http://www.youtube.com/watch?v=8MF4oJIHuQw">video</a> available and a <a href="https://wiki.openstreetmap.org/wiki/Fehlerbereinigung_mit_Hilfe_von_keepright.at">detailed tutorial</a>, the latter unfortunately only in German.</p>
</div>
<div id="comment-16567-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 09:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="16568"></span>
<div id="comment-16568" class="comment">
<div id="post-16568-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks scai and stephan75.... Very informative</p>
</div>
<div id="comment-16568-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 10:35)</span> <span class="comment-user userinfo">JCsM</span>
</div>
</div>
<span id="16569"></span>
<div id="comment-16569" class="comment not_top_scorer">
<div id="post-16569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for so much usefull information, i didn't had any idea about this app to scan and correct errors.</p>
</div>
<div id="comment-16569-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 11:40)</span> <span class="comment-user userinfo">Juan Facundo</span>
</div>
</div>
<span id="16571"></span>
<div id="comment-16571" class="comment">
<div id="post-16571-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Another tool to find routing problems, similar to keeplright is <a href="http://tools.geofabrik.de/osmi/?view=routing">http://tools.geofabrik.de/osmi/?view=routing</a></p>
</div>
<div id="comment-16571-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 11:53)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="16590"></span>
<div id="comment-16590" class="comment not_top_scorer">
<div id="post-16590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Vincent I will try that one too</p>
</div>
<div id="comment-16590-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 23:02)</span> <span class="comment-user userinfo">JCsM</span>
</div>
</div>
</div>
<div id="comment-tools-16560" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-16560-form-container" class="comment-form-container">
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


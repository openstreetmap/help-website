+++
type = "question"
title = "One lake with two names"
description = '''Hi, there is a lake in Sweden (Jämtlands län, near Käringsjön) that appears to have two names. One for the western part (Väster-Rödsjön) and another name for the eastern part (Öster-Rödsjön). But it&#x27;s one body of water. So how do I map this? Do I have to split the body of water into two parts and cr...'''
date = "2021-10-17T15:03:00Z"
lastmod = "2021-10-17T19:36:00Z"
weight = 82199
keywords = [ "sweden", "naming", "lake", "mapping" ]
aliases = [ "/questions/82199" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [One lake with two names](/questions/82199/one-lake-with-two-names)

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
<span id="post-82199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82199-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>there is a lake in Sweden (Jämtlands län, near Käringsjön) that appears to have two names. One for the western part (Väster-Rödsjön) and another name for the eastern part (Öster-Rödsjön). But it's one body of water. So how do I map this? Do I have to split the body of water into two parts and create "two lakes" that touch each other? Or is there an easier way to get both names on the lake?</p>
<p>Here are two links to maps showing the lake in qustion: <a href="https://minkarta.lantmateriet.se/?e=362332&amp;n=6918890&amp;z=10&amp;profile=karta&amp;background=1&amp;boundaries=false">https://minkarta.lantmateriet.se/?e=362332&amp;n=6918890&amp;z=10&amp;profile=karta&amp;background=1&amp;boundaries=false</a> <a href="https://www.graenslandet.se/images/stories/kartor/karta_rogen.pdf">https://www.graenslandet.se/images/stories/kartor/karta_rogen.pdf</a></p>
<p>Cheers, telegnom</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sweden" rel="tag" title="see questions tagged &#39;sweden&#39;">sweden</span> <span class="post-tag tag-link-naming" rel="tag" title="see questions tagged &#39;naming&#39;">naming</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '21, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e4a485080b004cd1fcaf4ba5f86aa785?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="telegnom&#39;s gravatar image" />
<p><span>telegnom</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="telegnom has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82199" class="comments-container">
&#10;</div>
<div id="comment-tools-82199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82199-form-container" class="comment-form-container">
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

<span id="82200"></span>

<div id="answer-container-82200" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82200-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="telegnom has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a complicated process firstly because of the islands and secondly due to the fact that the way comprising the whole lake shares nodes with several existing multipolygons for wood and wetland areas. Mapping objects in this way is simpler in the beginning but becomes problematical when someone, later on, is faced with the chore of modifying it, as you will see.</p>
<p>The way comprising the entire water body outline must be divided at some logical point thus creating two separate multipolygons. The way that divides the two will be shared by both, that is, it will be a member of both lake multipolygons. When finished each lake would then have its own multipolygon containing different members and a different name; one will have the name Öster-Rödsjön the other the name Väster-Rödsjön.</p>
<p>Depending upon its location, each island, the inner areas, would then need to become a member of the appropriate multipolygon. They cannot be members of both. This process is tricky because of those inner members. If there were no islands (inners), it would be relatively much simpler. Also as I mentioned above, the original mapper used the simple method of duplicating nodes that belong to both the wood and lake multipolygons when creating the lake.</p>
<p>If I were doing this, I might simply delete the entire lake multipolygon and recreate it using pieces from those other multipolygons, each of which would then be shared between one of the new lakes and those wooded areas.</p>
<p>I hope this helps. Please ask for clarification if you are confused.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '21, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82200" class="comments-container">
<span id="82201"></span>
<div id="comment-82201" class="comment">
<div id="post-82201-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is exactly what I feared. Then I'll get to work on it the next few days and split the multipolygon.</p>
<p>I had the faint hope that there was a simpler solution.</p>
<p>Thank you for your detailed answer!</p>
</div>
<div id="comment-82201-info" class="comment-info">
<span class="comment-age">(17 Oct '21, 16:57)</span> <span class="comment-user userinfo">telegnom</span>
</div>
</div>
<span id="82202"></span>
<div id="comment-82202" class="comment">
<div id="post-82202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A much simpler (but terrible) way to do this is to simply use two nodes with the different lake names located approximately in the center of each lake. Remove the name from the overall water body after you do that. This would make the lakes findable by name in a Nominatim search but that's about the only good thing about this approach.</p>
<p>This is not a recommended practice. JOSM will complain about using tags like natural=water on a node rather than an area and you would probably get pushback from some mapper in the future.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div id="comment-82202-info" class="comment-info">
<span class="comment-age">(17 Oct '21, 17:17)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="82211"></span>
<div id="comment-82211" class="comment">
<div id="post-82211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, I'll to it the proper way. Quick'n'dirty hacks tend to explode someday sooner or later. ;) Cheers, telegnom</p>
</div>
<div id="comment-82211-info" class="comment-info">
<span class="comment-age">(17 Oct '21, 18:35)</span> <span class="comment-user userinfo">telegnom</span>
</div>
</div>
<span id="82213"></span>
<div id="comment-82213" class="comment">
<div id="post-82213-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks good to me - <a href="https://www.openstreetmap.org/relation/2315342">https://www.openstreetmap.org/relation/2315342</a> and <a href="https://www.openstreetmap.org/relation/13335798">https://www.openstreetmap.org/relation/13335798</a> , joined by <a href="https://www.openstreetmap.org/way/993479645#map=18/62.36690/12.34622">https://www.openstreetmap.org/way/993479645#map=18/62.36690/12.34622</a></p>
</div>
<div id="comment-82213-info" class="comment-info">
<span class="comment-age">(17 Oct '21, 19:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82200-form-container" class="comment-form-container">
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


+++
type = "question"
title = "`building:part=parking` -&gt; `parking=multi-story` within `building=yes`"
description = '''Have I tagged this building correctly? outline -&amp;gt; with the address, name and building:levels=8 building:part=retail -&amp;gt; building:levels=1 building:part=parking -&amp;gt; parking=multi-story, min_level:1, building:levels=3 building:part=residential -&amp;gt; min_level:3, building:levels=8  Then the park...'''
date = "2021-12-04T07:33:00Z"
lastmod = "2021-12-05T18:07:00Z"
weight = 82747
keywords = [ "building", "parking_entrance", "multi-storey", "parking" ]
aliases = [ "/questions/82747" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\`building:part=parking\` -\> \`parking=multi-story\` within \`building=yes\`](/questions/82747/buildingpartparking-parkingmulti-story-within-buildingyes)

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
<span id="post-82747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82747-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Have I tagged this <a href="https://www.openstreetmap.org/way/894616437#map=19/-33.92834/18.44303">building</a> correctly?</p>
<p>outline -&gt; with the <code>address, name and building:levels=8</code><br />
<code>building:part=retail</code> -&gt; <code>building:levels=1</code><br />
<code>building:part=parking</code> -&gt; <code>parking=multi-story, min_level:1, building:levels=3</code><br />
<code>building:part=residential</code> -&gt; <code>min_level:3, building:levels=8</code></p>
<p>Then the parking garage entrance -&gt; <code>parking=multi-story</code>.<br />
The entrance is obviously at ground level but parking is on the 1st and 2nd level.</p>
<p><img src="/upfiles/IMG_0275_-_Copy_RQo3NUP.JPG" alt="alt text" /></p>
<p>Would the same rational apply if the parking is underground?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-parking_entrance" rel="tag" title="see questions tagged &#39;parking_entrance&#39;">parking_entrance</span> <span class="post-tag tag-link-multi-storey" rel="tag" title="see questions tagged &#39;multi-storey&#39;">multi-storey</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '21, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a235da08f7d6877654b16dfe832aed66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arkriger&#39;s gravatar image" />
<p><span>arkriger</span><br />
<span class="score" title="155 reputation points">155</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arkriger has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '21, 12:46</strong> </span></p>
</div>
</div>
<div id="comments-container-82747" class="comments-container">
&#10;</div>
<div id="comment-tools-82747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82747-form-container" class="comment-form-container">
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

<span id="82749"></span>

<div id="answer-container-82749" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82749-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nice example, but I think it is incomplete and uses level tag in a way different from its typical usage:</p>
<ul>
<li>The multi-storey car park still needs an <code>amenity=parking</code> tag</li>
<li>Building levels usually assume the street level is <code>level=0</code>, with levels above having positive values &amp; below negative values. So the retail is <code>level=0</code>, the parking is <code>level=1;2</code> and the apartments are <code>level=3-7</code>.</li>
<li>There are no <code>building:levels</code> tags (<a href="https://wiki.openstreetmap.org/wiki/Key:building:levels">wikipage</a>). I'd expect building:levels=1 for retail, 2 for the car park and 4 or 5 (not clear to me) for the apartments</li>
<li>A level tag on the outline is not correct; you can use <code>building:levels</code> instead.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '21, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-82749" class="comments-container">
<span id="82754"></span>
<div id="comment-82754" class="comment">
<div id="post-82754-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.</p>
<p>I meant; <code>building:levels=*</code>.<br />
I've changed the question to more accurately reflect the challenge.</p>
<p><code>amenity=parking</code> it is.</p>
</div>
<div id="comment-82754-info" class="comment-info">
<span class="comment-age">(04 Dec '21, 11:02)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
<span id="82765"></span>
<div id="comment-82765" class="comment">
<div id="post-82765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think I understand why a node <code>amenity=parking</code> is preferred.</p>
<p>The <code>building:part=parking + amenity=parking</code> will <em>override</em> the <code>building name=*</code>. The building name will not render; only the P symbol.</p>
<p>I've dropped a <a href="https://www.openstreetmap.org/node/9312695051">node</a> <code>amenity=parking + parking=multi-story</code> while keeping the <code>building:part=parking + parking=multi-story</code>.</p>
<p>Is this bad practice? To duplicate in this way?<br />
Would removing the <code>parking=multi-story</code> from the <code>building</code> be better? - (since <code>building:part=parking</code> accounts for this)</p>
<p>Obviously where there are no conflicts <code>building:part=parking + parking=multi-story + amenity=parking + building:levels=*</code> would be the way to go.</p>
</div>
<div id="comment-82765-info" class="comment-info">
<span class="comment-age">(05 Dec '21, 18:07)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
</div>
<div id="comment-tools-82749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82749-form-container" class="comment-form-container">
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


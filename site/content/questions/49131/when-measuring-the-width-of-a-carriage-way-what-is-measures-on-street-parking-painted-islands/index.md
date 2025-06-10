+++
type = "question"
title = "When measuring the width of a carriage way, what is measures?  (on-street parking, painted islands)"
description = '''When measuring the width of a way, do you measure from gutter to gutter, or shoulder-line to shoulder-line, for example; or, do you exclude the area taken up by habitual on-street parking?'''
date = "2016-04-09T11:34:00Z"
lastmod = "2016-04-10T21:58:00Z"
weight = 49131
keywords = [ "width", "measurement", "carriageway", "parking" ]
aliases = [ "/questions/49131" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [When measuring the width of a carriage way, what is measures? (on-street parking, painted islands)](/questions/49131/when-measuring-the-width-of-a-carriage-way-what-is-measures-on-street-parking-painted-islands)

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
<span id="post-49131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49131-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When measuring the width of a way, do you measure from gutter to gutter, or shoulder-line to shoulder-line, for example; or, do you exclude the area taken up by habitual on-street parking?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span> <span class="post-tag tag-link-measurement" rel="tag" title="see questions tagged &#39;measurement&#39;">measurement</span> <span class="post-tag tag-link-carriageway" rel="tag" title="see questions tagged &#39;carriageway&#39;">carriageway</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '16, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/f31a532b1c1cfe1c45a34ef352ffac51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samuelrussell&#39;s gravatar image" />
<p><span>samuelrussell</span><br />
<span class="score" title="116 reputation points">116</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samuelrussell has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49131" class="comments-container">
&#10;</div>
<div id="comment-tools-49131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49131-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="49134"></span>

<div id="answer-container-49134" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49134-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would measure the with from kerb to kerb or end of the paved area if there is no kerb.</p>
<p><span><img src="//wiki.openstreetmap.org/w/images/thumb/1/16/Width_at_6044_-_Meiringen_-_Kirchgasse.jpg/500px-Width_at_6044_-_Meiringen_-_Kirchgasse.jpg" alt="street with overlaid measurement arrows" /></span><br />
<span class="small">(own illustration based on a photo by Thisisbossi, license: <span>CC BY-SA 3.0</span>)</span></p>
<p>That there is street parking possible can be indicated by a tag with the key <span><code>parking:lane</code></span>. That there is a shoulder can be indicated by a tag with the key <span><code>shoulder</code></span>. All those are part of a street, are they not? … and users of the data could take those extra tags into account (e.g. when calculating if a over-width vehicle can use this street).</p>
<p>Definitely I would include the parking space if it is subtracted from what is a driving lane if no one parks there ... I am not that sure about the shoulder. If there is a <code>shoulder</code> tag on the highway way I would assume that the width includes the shoulder, as it is mapped as the same object which carries the width. A bit questionable what to think if there is no <code>shoulder</code> tag. And I think, we have no definition of what to include in the width of a "<code>highway</code>".</p>
<p>Some further thoughts: Okay, so, what if a way with a <code>highway</code> tag and a <code>width</code> tag also has a <span><code>sidewalk</code></span> tag? Since the <code>width</code> tag is tagged on the way it applies to the whole way – so, if the way includes a <code>sidewalk=both</code> then <code>width</code> needs to include the sidewalk. Mindblowing... More specific width tags may make more sense, I guess. <a href="https://taginfo.openstreetmap.org/keys/?key=width:carriageway"><code>width:carriageway</code></a> (184 uses) maybe?</p>
<p>We have currently 2037 <a href="https://taginfo.openstreetmap.org/keys/width%3Alanes"><code>width:lanes</code></a> tags, which likely specify the width of the single <span>lanes</span> (see the values at taginfo, too). Maybe specifying this makes more sense – depending on your use case.</p>
<p>Or tag the width of the shoulder in addition to the overall width: <a href="https://taginfo.openstreetmap.org/keys/width%3Ashoulder"><code>width:shoulder</code></a> (881 uses) or <a href="https://taginfo.openstreetmap.org/keys/shoulder%3Awidth"><code>shoulder:width</code></a> (1906 uses).</p>
<p>I assume, that in the beginning of OSM, when there were no <code>sidewalk</code>s, parking lanes, <code>shoulder</code>s and stuff tagged onto the same object on which the <code>highway</code> tag was on, the <code>width</code> just meant the width of the carriageway (possibly including such facultative parking like in the photo). While writing this answer I more or less came to the conclusion that, nowadays, a unspecified <code>width</code> tag does not make much sense for ways which have a highway tag, because it is not clear what is meant by it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '16, 21:30</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '16, 11:29</strong> </span></p>
</div>
</div>
<div id="comments-container-49134" class="comments-container">
<span id="49141"></span>
<div id="comment-49141" class="comment">
<div id="post-49141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for <code>width:carriageway</code> in particular.</p>
</div>
<div id="comment-49141-info" class="comment-info">
<span class="comment-age">(10 Apr '16, 07:28)</span> <span class="comment-user userinfo">samuelrussell</span>
</div>
</div>
<span id="49147"></span>
<div id="comment-49147" class="comment">
<div id="post-49147-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to be a little careful with some of these taginfo numbers - in some cases they've been created either mechanically or by humans, but without brain being in gear. For example, I randomly picked a "shoulder:width" and got to <a href="http://www.openstreetmap.org/way/391523093">http://www.openstreetmap.org/way/391523093</a> . Obviously (both logically and from the imagery) there's no shoulder at all here - clearly the way for the main carriageway has been split and the extra tags simply haven't been noticed.</p>
</div>
<div id="comment-49147-info" class="comment-info">
<span class="comment-age">(10 Apr '16, 10:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49154"></span>
<div id="comment-49154" class="comment">
<div id="post-49154-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse"></a><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: thanks for the note, indeed, I quoted those numbers just for ease of reading (no need to click through to taginfo each time if you want to know the number). High numbers do not necessarily mean that a tag is used by many mappers or is useful and well-thought-out at all.</p>
</div>
<div id="comment-49154-info" class="comment-info">
<span class="comment-age">(10 Apr '16, 11:10)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49134-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49143"></span>

<div id="answer-container-49143" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49143-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I read the following:</p>
<ul>
<li><code>width</code> = undefined, OR, a, OR c, OR f, OR m+n</li>
<li><code>roadreserve:width</code> = a</li>
<li><code>sidewalk:width</code> = b or j, thus :left &amp; :right</li>
<li><code>width:road</code> = f</li>
<li><code>width:carriageway</code> = m+n</li>
<li><code>width:lane:forward</code> = m</li>
<li><code>width:lane:backward</code> = n</li>
<li><code>parking:lane:left:width</code> = g</li>
<li><code>parking:lane:right:perpendicular:off-road:length</code> = d</li>
<li><code>shoulder:width:left</code> = g</li>
<li><code>shoulder:width:right</code> = d or h, depending on the way</li>
<li><code>traffic_calming:island:width</code> = k</li>
<li><code>cycleway:backward:lane:width</code> = i</li>
<li><code>width:verge</code> = e</li>
</ul>
<p><img src="/upfiles/width_1_Birriga_Road_NSW.png" alt="LPI NSW Base Map, Birriga Road NSW" /> <img src="/upfiles/width_2_Birriga_Road_NSW.jpg" alt="LPI NSW Imagery, Birriga Road NSW" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '16, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/f31a532b1c1cfe1c45a34ef352ffac51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samuelrussell&#39;s gravatar image" />
<p><span>samuelrussell</span><br />
<span class="score" title="116 reputation points">116</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samuelrussell has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '16, 11:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</img>
</div>
</div>
<div id="comments-container-49143" class="comments-container">
<span id="49148"></span>
<div id="comment-49148" class="comment">
<div id="post-49148-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Whilst you can of course use any tags you like, a quick look at the usage of <a href="https://taginfo.openstreetmap.org/keys/parking%3Alane%3Aleft%3Awidth">https://taginfo.openstreetmap.org/keys/parking%3Alane%3Aleft%3Awidth</a> shows that only 3 mappers worldwide are using it. It's likely that the only maps using that data will be ones that they create.</p>
<p>"roadreserve:width" isn't used at all; you'd need to both explain what it meant and persuade other people that it's useful with that one.</p>
</div>
<div id="comment-49148-info" class="comment-info">
<span class="comment-age">(10 Apr '16, 10:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49162"></span>
<div id="comment-49162" class="comment">
<div id="post-49162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm more pointing out the variety of objects that a <code>width</code> on a way might point to. The wiki isn't particularly good source to inform tagging style here. Neither, for that matter, is the :lanes suffix style.</p>
</div>
<div id="comment-49162-info" class="comment-info">
<span class="comment-age">(10 Apr '16, 21:58)</span> <span class="comment-user userinfo">samuelrussell</span>
</div>
</div>
</div>
<div id="comment-tools-49143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49143-form-container" class="comment-form-container">
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


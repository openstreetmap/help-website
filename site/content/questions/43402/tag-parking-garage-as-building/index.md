+++
type = "question"
title = "Tag parking garage as building?"
description = '''I haven&#x27;t found clear guidance on this yet, but would like to know if there&#x27;s a best practice here.  For multi-level parking, the presets are usually amenity=parking, parking=multi-storey. For multi-level concrete structure dedicated solely to car parking, should it also have building=yes? That way,...'''
date = "2015-06-04T16:02:00Z"
lastmod = "2019-10-29T20:59:00Z"
weight = 43402
keywords = [ "building", "tagging", "parking" ]
aliases = [ "/questions/43402" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Tag parking garage as building?](/questions/43402/tag-parking-garage-as-building)

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
<span id="post-43402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43402-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I haven't found clear guidance on this yet, but would like to know if there's a best practice here.</p>
<p>For multi-level parking, the presets are usually amenity=parking, parking=multi-storey.</p>
<p>For multi-level concrete structure dedicated solely to car parking, should it also have building=yes? That way, it would show up on OSM Mapnik as a building, not just a yellow area, and would it would make sense to have building:levels and such. But none of the presets I've seen include a checkbox for building and some map styles may assume that amenity=parking and building=yes are mutually exclusive.</p>
<p>Edit: There is also no guidance in the wiki page for amenity=parking: <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '15, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ddcafc797cab5600d5044d989e36b1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erjiang&#39;s gravatar image" />
<p><span>erjiang</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erjiang has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '15, 17:19</strong> </span></p>
</div>
</div>
<div id="comments-container-43402" class="comments-container">
&#10;</div>
<div id="comment-tools-43402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43402-form-container" class="comment-form-container">
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

<span id="43408"></span>

<div id="answer-container-43408" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43408-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-43408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer: yes, tag it as amenity=parking, parking=multi-storey, and building=*.</p>
<p>This is quite common. Of the 20K parking=multi-storey objects, nearly half (about 9K) also have a building tag: <a href="http://taginfo.openstreetmap.org/tags/parking=multi-storey#combinations">http://taginfo.openstreetmap.org/tags/parking=multi-storey#combinations</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '15, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-43408" class="comments-container">
&#10;</div>
<div id="comment-tools-43408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43408-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43403"></span>

<div id="answer-container-43403" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43403-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a car park near here which is partly <a href="http://www.openstreetmap.org/way/72855139">ground level open parking</a>, and <a href="http://www.openstreetmap.org/way/72855168">partly multi-storey</a> - I added <code>building=carpark</code> in this example, though it has the same effect as <code>building=yes</code> in most use cases that I am aware of.</p>
<p>I probably added the building tag manually afterwards (and yes, building levels would probably also have been a good one to add)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '15, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '15, 16:11</strong> </span></p>
</div>
</div>
<div id="comments-container-43403" class="comments-container">
<span id="60852"></span>
<div id="comment-60852" class="comment">
<div id="post-60852-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>I believe <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dparking"><code>building=parking</code></a> might be a better tag here. According to taginfo, it is used on 689 features, compared to 10 for <code>building=carpark</code>.</p>
</div>
<div id="comment-60852-info" class="comment-info">
<span class="comment-age">(29 Nov '17, 04:05)</span> <span class="comment-user userinfo">wislander</span>
</div>
</div>
</div>
<div id="comment-tools-43403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43403-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71337"></span>

<div id="answer-container-71337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71337-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I recently had the same problem. JOSM doesn't know <code>building=parking</code> and/or <code>building=carpark</code>. If those are buildings where you pay for parking (which is mostly the case), I tag them as <code>building=commercial</code>, since it's essentially a business.</p>
<p>Tbf, I'm kinda tempted to just tag it as <code>building=yes</code>. No option is really fitting adequately, I feel like.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '19, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/fb7188d8be002ece64870dffe9ec6fa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="polemon&#39;s gravatar image" />
<p><span>polemon</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="polemon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71337" class="comments-container">
<span id="71356"></span>
<div id="comment-71356" class="comment">
<div id="post-71356-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>You can use any value you like in a tag. You aren't limited to just the values that JOSM includes in its presets. If building=parking best represents the form of the building, then by all means use that.</p>
</div>
<div id="comment-71356-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 15:58)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="71368"></span>
<div id="comment-71368" class="comment">
<div id="post-71368-score" class="comment-score">
6
</div>
<div class="comment-text">
<p>I would like to stress that setting building=parking does not obviate the need to set amenity=parking (unless you don't mind the parking to disappear from most maps). It is already difficult enough for style developers to implement rendering for hundreds of objects, let alone take into account rules like "if there isn't an amenity=parking tag, but the building is tagged building=parking, draw a 'P' on it" to cope with incomplete or non-standard tagging...</p>
</div>
<div id="comment-71368-info" class="comment-info">
<span class="comment-age">(29 Oct '19, 17:10)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="71375"></span>
<div id="comment-71375" class="comment">
<div id="post-71375-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, buildings originally designed as parking buildings do sometimes get a different, second use. The building in which <a href="https://www.openstreetmap.org/node/5760226143">https://www.openstreetmap.org/node/5760226143</a> sites was originally a "car park" for horses and carriages. It's now a trendy office building, but the former high entrances to let tall carriages in and out are still visible.</p>
</div>
<div id="comment-71375-info" class="comment-info">
<span class="comment-age">(29 Oct '19, 20:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71337-form-container" class="comment-form-container">
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


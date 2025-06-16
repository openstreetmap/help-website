+++
type = "question"
title = "How to Mark the Town Hall Perimeter"
description = '''Dear OSMers, I am working on improving OSM in Kermanshah, Iran and have come across a problem that needs your attention. The town hall is comprised of a couple of small size buildings enclosed in a sizeable piece of land, the premier of which is walled and restricted to public access. Here is the lo...'''
date = "2015-02-10T11:58:00Z"
lastmod = "2015-02-10T16:27:00Z"
weight = 40920
keywords = [ "landuse", "mapping", "tagging", "area" ]
aliases = [ "/questions/40920" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to Mark the Town Hall Perimeter](/questions/40920/how-to-mark-the-town-hall-perimeter)

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
<span id="post-40920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40920-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OSMers,</p>
<p>I am working on improving OSM in Kermanshah, Iran and have come across a problem that needs your attention. The town hall is comprised of a couple of small size buildings enclosed in a sizeable piece of land, the premier of which is walled and restricted to public access. Here is the location on OSM: <a href="https://www.openstreetmap.org/way/326821789">https://www.openstreetmap.org/way/326821789</a></p>
<p>I'd like to mark the entire premises as the town hall, rather than the individual buildings within. Something more flexible than the landuse tag. It's because First, the aerial resolution of Bing images leaves much to be desired. Second, I have no idea about the use and function of their buildings.</p>
<p>Here are the different things I have tried so far:</p>
<ol>
<li>Draw a polygon and mark it as amenity=townhall and building=yes. This gets drawn nicely on the map but is semantically wrong. Because it treats the land as one giant building.</li>
<li>Do as above but set building=no or remove it altogether. The location disappears on the rendered map. Not desirable.</li>
<li>Do as No 2 but add barrier=wall to the polygon. Now only the outline of the location is drawn, no names or any telling sign.</li>
</ol>
<p>Any suggestion and advice much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '15, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/66a871a98df58bf30465f92a297ac6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AmZaf&#39;s gravatar image" />
<p><span>AmZaf</span><br />
<span class="score" title="55 reputation points">55</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AmZaf has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '15, 12:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40920" class="comments-container">
<span id="40930"></span>
<div id="comment-40930" class="comment">
<div id="post-40930-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you all for the responses. As <a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> pointed out, it seems to be a rendering issue. At least I'm now sure that I was on the right track. However, until the rendering issues are sorted out many people might resort to ugly hacks to get items shown on the map. It's strange that landuse areas are rendered in distinct colours, while Office, Historic, and Amenity features without the accompanying building tags are completely ignored, even if these features have names on them (as in <a href="https://www.openstreetmap.org/way/49781808">example 2</a> above).</p>
<p>Maybe I should raise the issue with the OSM team. The way the standard layer is rendered, discourages my particular approach. Anyone knows how to file a bug report?</p>
</div>
<div id="comment-40930-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 14:16)</span> <span class="comment-user userinfo">AmZaf</span>
</div>
</div>
<span id="40935"></span>
<div id="comment-40935" class="comment">
<div id="post-40935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>bug report for the standard map style: see <span>there</span> or <a href="/questions/6241/change-request-adding-a-feature-to-the-default-osm-map-style">there</a>.</p>
</div>
<div id="comment-40935-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 16:27)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40920-form-container" class="comment-form-container">
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

<span id="40922"></span>

<div id="answer-container-40922" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40922-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Suggestion:</p>
<ul>
<li><code>amenity=townhall</code> on a closed way around the "entire premises". You could add a <code>barrier=wall</code> tag too (maybe on a separate way, so you could add area=no to make clear that it is no area, although this would not be needed for most renderers, I guess).</li>
<li>If possible (aerial imagery suffuciencent): Add the single buildings as usual (with <code>building=civic</code>).</li>
</ul>
<p>Do you mean this with your option 2? Then the rendered map (the one you are looking at) should be improved (and not your tagging). On the "Humanitarian" <a href="https://wiki.openstreetmap.org/wiki/Browsing#Layers">map</a> this is rendered as a symbol in the middle of the area. <a href="https://www.openstreetmap.org/way/146324989">Example 1</a>, <a href="https://www.openstreetmap.org/way/49781808">Example 2</a>. As far as I know the standard map has recently got a style update regarding those symbols, maybe those places would soon also show up on the standard map. Update: ah, now the icon appears at example 1 on zoom levels 17+ and at example 2 at zoom 18. So, you picked out a nice example of where just mapping/tagging "right" is the best way (instead of doing it somehow else, just because one map does not show it otherwise).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '15, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '15, 12:41</strong> </span></p>
</div>
</div>
<div id="comments-container-40922" class="comments-container">
<span id="40929"></span>
<div id="comment-40929" class="comment">
<div id="post-40929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. My option 2 is the same (no building tag). You are right, it seems to be a rendering issue.</p>
</div>
<div id="comment-40929-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 13:34)</span> <span class="comment-user userinfo">AmZaf</span>
</div>
</div>
</div>
<div id="comment-tools-40922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40922-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40923"></span>

<div id="answer-container-40923" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likel the best solution to your problem from a data perspective is likely a site relation <a href="https://wiki.openstreetmap.org/wiki/Relation:site">https://wiki.openstreetmap.org/wiki/Relation:site</a> (no idea how it gets rendered though).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '15, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '15, 12:28</strong> </span></p>
</div>
</div>
<div id="comments-container-40923" class="comments-container">
<span id="40924"></span>
<div id="comment-40924" class="comment">
<div id="post-40924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is all at one continuous location/area, not at separate places, isn't it? So there is no need for a relation of any type.</p>
</div>
<div id="comment-40924-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 12:25)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40925"></span>
<div id="comment-40925" class="comment">
<div id="post-40925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Depends the intention of the site relation is to group all buildings landuse etc that belongs to one facility (avoiding for example multiple name labels etc).</p>
</div>
<div id="comment-40925-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 12:30)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="40926"></span>
<div id="comment-40926" class="comment">
<div id="post-40926-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Right, but here, we likely will not even get buildings ("the aerial resolution of Bing images leaves much to be desired"), and if everything is at one place (even without holes) it does not hurt to just use the simple thing of a closed way, IMHO.</p>
</div>
<div id="comment-40926-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 12:33)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40931"></span>

<div id="answer-container-40931" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There has been <a href="https://lists.openstreetmap.org/pipermail/tagging/2014-March/016842.html">discussion on the tagging list</a> of a landuse value for government administration buildings and surrounding land, and a <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/landuse%3Dcivic">proposal</a> (see also the talk page), but as far as I know, it hasn't come to any consensus yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '15, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-40931" class="comments-container">
&#10;</div>
<div id="comment-tools-40931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40931-form-container" class="comment-form-container">
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


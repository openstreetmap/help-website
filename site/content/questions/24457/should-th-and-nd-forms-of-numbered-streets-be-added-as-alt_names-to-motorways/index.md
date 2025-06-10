+++
type = "question"
title = "Should &quot;th&quot; and &quot;nd&quot; forms of numbered streets be added as alt_names to motorways?"
description = '''I&#x27;m new to editing and am trying to make sure that an address like, &quot;10185 90th Street NW, Edmonton, Canada&quot;  will geocode correctly. Right now, this search doesn&#x27;t find any results. If I change it to, &quot;10185 90 Street NW, Edmonton, Canada&quot;  the same search returns the correct results. The problem i...'''
date = "2013-07-22T17:06:00Z"
lastmod = "2013-07-24T13:24:00Z"
weight = 24457
keywords = [ "motorway", "nominatim", "geocoding" ]
aliases = [ "/questions/24457" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should "th" and "nd" forms of numbered streets be added as alt_names to motorways?](/questions/24457/should-th-and-nd-forms-of-numbered-streets-be-added-as-alt_names-to-motorways)

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
<span id="post-24457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24457-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to editing and am trying to make sure that an address like,</p>
<pre><code>&quot;10185 90th Street NW, Edmonton, Canada&quot;</code></pre>
<p>will geocode correctly. Right now, this search doesn't find any results. If I change it to,</p>
<pre><code>&quot;10185 90 Street NW, Edmonton, Canada&quot;</code></pre>
<p>the same search returns the correct results. The problem is that I know people typically include "th" and "nd" suffix on many street names here in Canada so technically, the first search is valid. For example, my Mom will write "90th Street" on mail to our address. What is the best way to correct this problem? I've searched for "90 Street" and found dozens of segments which would need to be edited to add the correct suffix. It would probably also be correct to add this suffix to other streets and avenues in most locations in Canada, in which case it require editing thousands of segments.</p>
<p>Should I use alt_name on each motorway segment? Is there a better way to handle this? What about modifying Nominatim to understand number suffixes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-motorway" rel="tag" title="see questions tagged &#39;motorway&#39;">motorway</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '13, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ea0af3fb97e5e13e95968859739108a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markbennett&#39;s gravatar image" />
<p><span>markbennett</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markbennett has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24457" class="comments-container">
&#10;</div>
<div id="comment-tools-24457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24457-form-container" class="comment-form-container">
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

<span id="24483"></span>

<div id="answer-container-24483" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24483-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="markbennett has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While you may want to check with a local (or at least north-american) mapper, writing "90th" instead of "90" seems like the right thing to do, as it cannot be read aloud naturally otherwise. So I'd use "90th" in the name tag, an maybe even forgo the use of an alt_name for "90" unless you find evidence that it is used in some cases. Try contacting the original mapper of those streets, or a local mailing-list to see if anybody defends the "90" spelling.</p>
<p>Regarding how to make the change, yes you need to do it on every segment of the street if it has been split in multiple osm ways. You can use shift-click to select multiple ways in your editor, and change the name of all of them in one go. If you use the JOSM editor, you can even use ctrl-f to search and select "name=.*90 Street.*" for example, if you prefer typing to clicking.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '13, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '13, 14:29</strong> </span></p>
</div>
</div>
<div id="comments-container-24483" class="comments-container">
<span id="24492"></span>
<div id="comment-24492" class="comment">
<div id="post-24492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick reply <span>@vincent</span>. It's disappointing to hear that the streets will need to be edited manually as there are many segments in my area. Hearing that it's possible to do with JOSM gives me hope however.</p>
<p>I'll start a discussion at the local level on the wiki as I believe the streets were all imported from a data export from the Canadian Government.</p>
</div>
<div id="comment-24492-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 18:12)</span> <span class="comment-user userinfo">markbennett</span>
</div>
</div>
<span id="24493"></span>
<div id="comment-24493" class="comment">
<div id="post-24493-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Suggest using the talk-ca mailing list rather than the wiki - OSM doesn't generally use wiki talk pages for in-project communication and people are likely to miss your message if it's posted there.</p>
</div>
<div id="comment-24493-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 18:27)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24483-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24530"></span>

<div id="answer-container-24530" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24530-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This sounds like it should be addressed on the nominatim (read: search engine) level, not necessarily in the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '13, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-24530" class="comments-container">
&#10;</div>
<div id="comment-tools-24530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24530-form-container" class="comment-form-container">
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


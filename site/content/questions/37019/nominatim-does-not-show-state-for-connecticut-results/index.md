+++
type = "question"
title = "[closed] Nominatim does not show state for Connecticut results"
description = '''Searching for &#x27;Ridgefield&#x27; Results in:  Town Ridgefield, Fairfield County, United States of America ... City Ridgefield, Clark County, Washington, United States of America  Other Ridgefield&#x27;s show the State, but the State seems missing from most of Connecticut&#x27;s results. Is the state boundary intact...'''
date = "2014-09-23T22:42:00Z"
lastmod = "2014-09-25T09:42:00Z"
weight = 37019
keywords = [ "nominatim" ]
aliases = [ "/questions/37019" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Nominatim does not show state for Connecticut results](/questions/37019/nominatim-does-not-show-state-for-connecticut-results)

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
<span id="post-37019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37019-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Searching for '<a href="http://www.openstreetmap.org/search?query=Ridgefield">Ridgefield</a>'</p>
<p>Results in:</p>
<ul>
<li>Town Ridgefield, Fairfield County, United States of America ...</li>
<li>City Ridgefield, Clark County, Washington, United States of America</li>
</ul>
<p>Other Ridgefield's show the State, but the State seems missing from most of Connecticut's results. Is the state boundary intact / closed? How can one tell?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '14, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f221969d01bf7d2a0707c85897d84ec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brianegge&#39;s gravatar image" />
<p><span>brianegge</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brianegge has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>25 Sep '14, 16:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-37019" class="comments-container">
<span id="37023"></span>
<div id="comment-37023" class="comment">
<div id="post-37023-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The Connecticut border is currently complete so that is not the issue.</p>
</div>
<div id="comment-37023-info" class="comment-info">
<span class="comment-age">(24 Sep '14, 11:05)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="37024"></span>
<div id="comment-37024" class="comment">
<div id="post-37024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't find the reason either. In Nominatim's internal representation <a href="http://nominatim.openstreetmap.org/details.php?place_id=9182658271">Connecticut</a> has similar properties like other states (e.g. <a href="http://nominatim.openstreetmap.org/details.php?place_id=97997829">New Jersey</a>) except that the <em>Parent Of</em> section is completely missing. Maybe Nominatim had some problems processing the relation?</p>
</div>
<div id="comment-37024-info" class="comment-info">
<span class="comment-age">(24 Sep '14, 12:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="37036"></span>
<div id="comment-37036" class="comment">
<div id="post-37036-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>There seems to be an issue with CT in the nominatim DB, it is being looked in to.</p>
</div>
<div id="comment-37036-info" class="comment-info">
<span class="comment-age">(24 Sep '14, 17:59)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37019-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by Pieren 25 Sep '14, 16:02

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37049"></span>

<div id="answer-container-37049" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37049-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Works now.</p>
<p>The issue seems to have been that when the data was imported in to the current nominatim instance the border was broken leading to it missing alltogether.</p>
<p>Note: I'm just playing the messenger here, the nominatim sys admins and devs did the work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '14, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '14, 14:41</strong> </span></p>
</div>
</div>
<div id="comments-container-37049" class="comments-container">
&#10;</div>
<div id="comment-tools-37049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37049-form-container" class="comment-form-container">
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


+++
type = "question"
title = "How do I correctly name a road bridge?"
description = '''How should I tag a named bridge that carries a (differently) named road? For example, in Newcastle there is a bridge across the Tyne called &quot;Swing Bridge&quot; which carries a tertiary road called &quot;Bridge Street&quot;.  The current tagging is just: highway=tertiary bridge=yes name=Swing Bridge  which works, b...'''
date = "2011-08-25T15:25:00Z"
lastmod = "2021-01-01T17:40:00Z"
weight = 7304
keywords = [ "name", "tagging" ]
aliases = [ "/questions/7304" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [How do I correctly name a road bridge?](/questions/7304/how-do-i-correctly-name-a-road-bridge)

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
<span id="post-7304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7304-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-7304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should I tag a named bridge that carries a (differently) named road?</p>
<p>For example, in Newcastle there is a bridge across the Tyne called "Swing Bridge" which carries a tertiary road called "Bridge Street".</p>
<p>The current tagging is just:</p>
<pre><code>highway=tertiary
bridge=yes
name=Swing Bridge</code></pre>
<p>which works, but doesn't record the name of the street. The name of the bridge is useful, as that is how locals would give you directions and is probably what should be rendered on the map, but the street name is also potentially useful - especially when searching.</p>
<p>Do we have any established technique for recording both names?</p>
<p>I'm guessing a similar problem exists for other named bridges and there may be worse case (e.g. I could imagine a named bridge that carrys several different named ways)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '11, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-7304" class="comments-container">
&#10;</div>
<div id="comment-tools-7304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7304-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="7317"></span>

<div id="answer-container-7317" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7317-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-7317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GrahamS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bridges can be mapped as areas tagged with the widely-supported <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dbridge"><code>man_made=bridge</code></a> tag. By mapping the bridge and the road as separate objects, each object can carry its own <code>name</code> tag. (There is also the option of mapping the bridge as a <a href="http://wiki.openstreetmap.org/wiki/Relations/Proposed/Bridges_and_Tunnels">relation</a>, but this is rarely necessary.)</p>
<p>If the bridge is not (yet) mapped as a separate object, the <a href="https://wiki.openstreetmap.org/wiki/Key:bridge:name"><code>bridge:name</code></a> is commonly used on the road to record the name of the bridge it is running across.</p>
<p><em>(Best practices have evolved a lot in the decade since this question was asked and there are now well-established solutions. This answer was rewritten in 2021 to reflect these changes.)</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jan '21, 17:38</strong> </span></p>
</div>
</div>
<div id="comments-container-7317" class="comments-container">
&#10;</div>
<div id="comment-tools-7317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7317-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7306"></span>

<div id="answer-container-7306" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7306-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://taginfo.openstreetmap.org/keys/bridge_name#values">bridge_name</a> seems to be used quite a bit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-7306" class="comments-container">
&#10;</div>
<div id="comment-tools-7306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7306-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78175"></span>

<div id="answer-container-78175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78175-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The newer solution is "man_made=bridge" and "name=*". This can be nicely visualised in Carto map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jan '21, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e39830800041c01c0ad201916e2c4065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="strongwillow&#39;s gravatar image" />
<p><span>strongwillow</span><br />
<span class="score" title="65 reputation points">65</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="strongwillow has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78175" class="comments-container">
<span id="78176"></span>
<div id="comment-78176" class="comment">
<div id="post-78176-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You're right, I've updated the accepted answer accordingly as it was outdated. Upvoted! :)</p>
</div>
<div id="comment-78176-info" class="comment-info">
<span class="comment-age">(01 Jan '21, 17:40)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-78175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78175-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7308"></span>

<div id="answer-container-7308" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7308-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>you can create a relation for the bridge, look there: <a href="http://wiki.openstreetmap.org/wiki/Relations/Proposed/Bridges_and_Tunnels">http://wiki.openstreetmap.org/wiki/Relations/Proposed/Bridges_and_Tunnels</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-7308" class="comments-container">
&#10;</div>
<div id="comment-tools-7308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7308-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7325"></span>

<div id="answer-container-7325" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7325-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You also have;<br />
alt_name - when alternative name exists (which doesn't fit in one of the tags name above)<br />
loc_name - Locally known as</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 23:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f6827fbcbfc77428dfb7f8743ab775db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sundance&#39;s gravatar image" />
<p><span>Sundance</span><br />
<span class="score" title="467 reputation points">467</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sundance has one accepted answer">3%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>25 Aug '11, 23:52</strong> </span></p>
</div>
</div>
<div id="comments-container-7325" class="comments-container">
&#10;</div>
<div id="comment-tools-7325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7325-form-container" class="comment-form-container">
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


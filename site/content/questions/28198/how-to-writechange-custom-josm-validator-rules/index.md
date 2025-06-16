+++
type = "question"
title = "How to write/change custom JOSM validator rules?"
description = '''Is there any way of writing my own custom rules for the JOSM validator, or to change some of the existing rules? Sometimes, the default rules flag as &quot;warning&quot; lots of &quot;defects&quot; that really aren&#x27;t problems, because the underlying rule is not specific enough, or is too strict, and sometimes I want ne...'''
date = "2013-11-18T20:08:00Z"
lastmod = "2024-02-19T07:01:00Z"
weight = 28198
keywords = [ "rules", "josm", "validator", "custom" ]
aliases = [ "/questions/28198" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to write/change custom JOSM validator rules?](/questions/28198/how-to-writechange-custom-josm-validator-rules)

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
<span id="post-28198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28198-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-28198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way of writing my own custom rules for the JOSM validator, or to change some of the existing rules?</p>
<p>Sometimes, the default rules flag as "warning" lots of "defects" that really aren't problems, because the underlying rule is not specific enough, or is too strict, and sometimes I want new rules so that I can check my own work more strictly.</p>
<p>For example, the default rules flag the ways used for house number interpolation that end near a street corner as "Way end near other way", and while this is strictly true, these ways do not have real physical representation, and are just a helpful construct to aid in address geolocation. Therefore, I do not want them flagged as such, requiring one extra rule in the validation to exclude them. See <a href="/questions/26509/should-the-ways-that-generate-the-interpolated-address-numbers-from-the-known-points-cross-other-streets-or-not">this question</a> for more information. If I disable the "unconnected ways" option in the preferences page, or change the "validator.UnconnectedWays.node_way_distance" configuration value, the validator will miss the real unconnected ways...</p>
<p>Another example is for the recent change that flags as "warning" the missing voltage of power lines. See <a href="http://josm.openstreetmap.de/ticket/9332">here</a>. I do want to disable this rule (annoying!) in my local working copy, but if I disable the "power lines" option in the JOSM validator's preferences page, I would also disable all of the other errors/warnings related to power lines.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rules" rel="tag" title="see questions tagged &#39;rules&#39;">rules</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '13, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-28198" class="comments-container">
&#10;</div>
<div id="comment-tools-28198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28198-form-container" class="comment-form-container">
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

<span id="28211"></span>

<div id="answer-container-28211" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28211-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-28211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MCPicoli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know there isn't an "easy syntax" to create/modify validator tests (like there is for presets for example). You'll have to patch <a href="https://josm.openstreetmap.de/browser/josm/trunk/src/org/openstreetmap/josm/data/validation">this code</a> to modify an existing test or add a new one. Your example improvement of ignoring certain ways for the unconnected_ways test shouldn't be hard to do.</p>
<p>Once you've improved a validator test, upstream will certainly be happy to review and merge your patch, so that all users can benefit. Create a <a href="http://josm.openstreetmap.de/newticket">josm bug report</a> explaining why the change is needed and attaching your patch. Thanks in advance :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '13, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-28211" class="comments-container">
<span id="28212"></span>
<div id="comment-28212" class="comment">
<div id="post-28212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you aren't comfortable with software development workflows (downloading, compiling, comitting...) head over to <a href="https://wiki.openstreetmap.org/wiki/IRC">#osm-dev or #josm</a> to guide you. Have fun :)</p>
</div>
<div id="comment-28212-info" class="comment-info">
<span class="comment-age">(19 Nov '13, 10:07)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="28216"></span>
<div id="comment-28216" class="comment">
<div id="post-28216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems easy enough. I'll give it a try next weekend, work hours allowing.</p>
</div>
<div id="comment-28216-info" class="comment-info">
<span class="comment-age">(19 Nov '13, 11:39)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="28217"></span>
<div id="comment-28217" class="comment">
<div id="post-28217-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>WOW! Was just checking the code Vincent linked (hoping to understand it), and, to my surprise, there already was a patch (by Don-vip) for this case (for the bug report I opened yesterday)! Probably it'll be merged into the next "tested" version. Thanks anyway!</p>
</div>
<div id="comment-28217-info" class="comment-info">
<span class="comment-age">(19 Nov '13, 11:44)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-28211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28211-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84227"></span>

<div id="answer-container-84227" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84227-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With JOSM’s <a href="https://josm.openstreetmap.de/wiki/Help/Validator/MapCSSTagChecker">tag checker</a> it’s now possible to add your own custom validations using <a href="https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation">MapCSS</a>. For example:</p>
<ol>
<li><p>Create a file named <code>example.validator.mapcss</code> containing:</p>
<pre><code>*[&quot;addr:housenumber&quot;][!&quot;addr:state&quot;] {
  throwWarning: tr(&quot;Address missing state&quot;);
}</code></pre></li>
<li><p>Select the file in <em>JOSM → Edit → Preferences → Data validator → Tag checker rules → Add (+)</em>.</p></li>
</ol>
<p>When you run the validator (typically automatically before upload) you’ll get a warning:</p>
<blockquote>
<p><img src="/upfiles/Screenshot_from_2022-04-19_14-00-18.png" width="585" alt="screenshot" /></p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '22, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c1950a9357df3658d5473fdc05cb317a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Kvalheim&#39;s gravatar image" />
<p><span>Andrew Kvalheim</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Kvalheim has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-84227" class="comments-container">
&#10;</div>
<div id="comment-tools-84227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84227-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88246"></span>

<div id="answer-container-88246" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88246-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>would anyone be able to create a .mapcss file for validator to reveal the address (as a duplication) placed on the building as a node? (if any address tag already exists in the building)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '24, 07:01</strong></p>
<img src="https://secure.gravatar.com/avatar/176f2567c3da5fb061d49a9027c1db2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klerik7&#39;s gravatar image" />
<p><span>Klerik7</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klerik7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88246" class="comments-container">
&#10;</div>
<div id="comment-tools-88246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88246-form-container" class="comment-form-container">
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


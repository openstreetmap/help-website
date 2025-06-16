+++
type = "question"
title = "How would I go about automated mass tagging?"
description = '''How would I go about automated tagging? I am wondering how I can add a massive amount of tags to OSM to help improve the map in my area? For example, I would like to tag the speed limits and all residential roads that are 100M or smaller with the speed limit of 25miles per hour unless there it is a ...'''
date = "2012-11-07T15:34:00Z"
lastmod = "2012-11-08T12:56:00Z"
weight = 17561
keywords = [ "mass_tagging", "speedlimit", "bot", "policy" ]
aliases = [ "/questions/17561" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How would I go about automated mass tagging?](/questions/17561/how-would-i-go-about-automated-mass-tagging)

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
<span id="post-17561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17561-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would I go about automated tagging?</p>
<p>I am wondering how I can add a massive amount of tags to OSM to help improve the map in my area? For example, I would like to tag the speed limits and all residential roads that are 100M or smaller with the speed limit of 25miles per hour unless there it is a private road. This is something that would help the rout-ability and start the basis of time based routing. It would be very annoying to tag roads manually and automation is something that could aid this endeavor. I could also use state laws to construct other automated tagging. Does OSM have a bot that could do this if not would I have to write my own and if so who would I have to talk to to get the proper authority to do so. Also does anyone think this is a bad idea, if so why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mass_tagging" rel="tag" title="see questions tagged &#39;mass_tagging&#39;">mass_tagging</span> <span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-bot" rel="tag" title="see questions tagged &#39;bot&#39;">bot</span> <span class="post-tag tag-link-policy" rel="tag" title="see questions tagged &#39;policy&#39;">policy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '12, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/602a4908e9bea5a3f086bd91654717c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redsteakraw&#39;s gravatar image" />
<p><span>redsteakraw</span><br />
<span class="score" title="1040 reputation points"><span>1.0k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redsteakraw has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17561" class="comments-container">
&#10;</div>
<div id="comment-tools-17561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17561-form-container" class="comment-form-container">
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

<span id="17562"></span>

<div id="answer-container-17562" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17562-score" class="post-score" title="current number of votes">
15
</div>
<span id="post-17562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is "You don't".</p>
<p>Automated edits like this don't add anything to the data, since any users of the data could infer the same information you're adding by using the same rules you are. Mass, automated tagging is also inaccurate, since there are always exceptions to rules, and your code won't spot these.</p>
<p>Even if you could justify the principle of mass tagging using a bot, you'd have to demonstrate your code worked properly and did no harm. By the time you've done all that, you might as well have done the tagging by hand, more accurately and without problems.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '12, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-17562" class="comments-container">
&#10;</div>
<div id="comment-tools-17562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17562-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17563"></span>

<div id="answer-container-17563" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17563-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-17563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is a bad idea. If the speed limit, or indeed anything else, can be automatically inferred then it should not be tagged explicitly. You will only burden the database (and all its users) with that "massive amount" of tags, plus your tags will occasionally be wrong (since you're only guessing the max speed and not observing it).</p>
<p>You may think that this improves the map but it doesn't. Just like writing good prose - every word you can leave out without changing the essence of what is said will <em>improve</em> the text ;) It improves the map if you go out and add actually surveyed information, not if you write a bot and add tons of tags that do not add information but noise.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '12, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17563" class="comments-container">
<span id="17564"></span>
<div id="comment-17564" class="comment">
<div id="post-17564-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>If speed limits are set by State laws and every State has different laws(in the United States), is there anyway of adding these rules or speed hints to a State's administrative boundary, instead of mass tagging?</p>
</div>
<div id="comment-17564-info" class="comment-info">
<span class="comment-age">(07 Nov '12, 16:08)</span> <span class="comment-user userinfo">redsteakraw</span>
</div>
</div>
<span id="17577"></span>
<div id="comment-17577" class="comment">
<div id="post-17577-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is no established tagging scheme for maxspeed on boundary relations, so there is room to invent one. I propose to add</p>
<p>maxspeed:motorway</p>
<p>maxspeed:trunk</p>
<p>maxspeed:city</p>
<p>maxspeed:hgv</p>
<p>maxspeed</p>
<p>where the last one contains the default value, or maybe other descriptive tags.</p>
<p>Then please write some lines about that in the wiki. No proposal or so is required for this.</p>
</div>
<div id="comment-17577-info" class="comment-info">
<span class="comment-age">(08 Nov '12, 07:27)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="17584"></span>
<div id="comment-17584" class="comment">
<div id="post-17584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is a proposal here for tagging defaults: <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Defaults">https://wiki.openstreetmap.org/wiki/Relations/Proposed/Defaults</a></p>
<p>Also see this list of default speed limits for each country: <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed">https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed</a></p>
</div>
<div id="comment-17584-info" class="comment-info">
<span class="comment-age">(08 Nov '12, 12:56)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-17563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17563-form-container" class="comment-form-container">
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


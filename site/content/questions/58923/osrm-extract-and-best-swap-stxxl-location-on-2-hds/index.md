+++
type = "question"
title = "OSRM extract and best swap stxxl location on 2 HDs"
description = '''Hi, I want to set up the car profile data, but it is now taking 3 days and still at 100% Graphs (so way more to go) and I am thinking, maybe my swap and stxxl is just set up inappropriately. I have the following system  2 HDs 4 TB SATA 6 Gb/s 7200 rpm HDD Enterprise-Class 64 GB DDR4 RAM Intel® Core™...'''
date = "2017-09-02T09:10:00Z"
lastmod = "2017-09-07T15:41:00Z"
weight = 58923
keywords = [ "osrm-extract", "stxxl", "swap" ]
aliases = [ "/questions/58923" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSRM extract and best swap stxxl location on 2 HDs](/questions/58923/osrm-extract-and-best-swap-stxxl-location-on-2-hds)

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
<span id="post-58923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to set up the car profile data, but it is now taking 3 days and still at 100% Graphs (so way more to go) and I am thinking, maybe my swap and stxxl is just set up inappropriately.</p>
<p>I have the following system</p>
<ul>
<li>2 HDs 4 TB SATA 6 Gb/s 7200 rpm HDD Enterprise-Class</li>
<li>64 GB DDR4 RAM</li>
<li>Intel® Core™ i7-6700 Quad-Core Skylake incl. Hyper-Threading</li>
</ul>
<p>HD1 has the</p>
<ul>
<li>system</li>
<li>programs</li>
<li>osm.pbf file on it</li>
<li>the extracted data must go on this one</li>
<li>partition with 32G swap</li>
</ul>
<p>HD2 mostly is empty (but the space is going to be needed for some other big data)</p>
<p>My extract approach was to set up another swap of 300G on HD2 and stxxl of 300G on HD2. But it seems to be too slow. iotop has some reading and some writing activity on it, but nothing major. htop does not show any significant cpu usage. I start with 8 processes.</p>
<ol>
<li>Is there a better way to set up the additional swap and stxxl (maybe the swap on HD1 and only the stxxl on HD2)?</li>
<li>If I could move the files and target locations of the extracted data as wanted, would it be even better to maybe do .pbf on HD1, all swap and stxxl on HD1 and extracted data on hd2(and then just copy it to HD1)?</li>
</ol>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm-extract" rel="tag" title="see questions tagged &#39;osrm-extract&#39;">osrm-extract</span> <span class="post-tag tag-link-stxxl" rel="tag" title="see questions tagged &#39;stxxl&#39;">stxxl</span> <span class="post-tag tag-link-swap" rel="tag" title="see questions tagged &#39;swap&#39;">swap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '17, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e9400940cd6333c87b0403174a213707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wordli&#39;s gravatar image" />
<p><span>wordli</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wordli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58923" class="comments-container">
<span id="58959"></span>
<div id="comment-58959" class="comment">
<div id="post-58959-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How large is the input file (.osm.pbf file)? Do you try to process the whole planet?</p>
<p>You might have a look at <a href="https://lists.openstreetmap.org/pipermail/osrm-talk/2017-July/001460.html">https://lists.openstreetmap.org/pipermail/osrm-talk/2017-July/001460.html</a> for RAM requirements.</p>
</div>
<div id="comment-58959-info" class="comment-info">
<span class="comment-age">(04 Sep '17, 09:41)</span> <span class="comment-user userinfo">Nakaner</span>
</div>
</div>
<span id="58969"></span>
<div id="comment-58969" class="comment">
<div id="post-58969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, I am processing the whole planet (37G)</p>
</div>
<div id="comment-58969-info" class="comment-info">
<span class="comment-age">(04 Sep '17, 19:00)</span> <span class="comment-user userinfo">wordli</span>
</div>
</div>
</div>
<div id="comment-tools-58923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58923-form-container" class="comment-form-container">
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

<span id="58971"></span>

<div id="answer-container-58971" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58971-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Processing the full planet with the default car profile will take more than 150 GB of RAM. In your case, with 64 GB of RAM and 32 GB of swap, I'd expect it to die at some point; you'd need 96 GB of swap to even make it work and then it would take very long.</p>
<p>One way of saving memory is splitting the planet up into disjunct areas, of course at the cost of not being able to route between them later on. Or you could use a different routing software that has a lesser memory footprint (but might then be slower to run).</p>
<p>64 GB of RAM should be enough to <em>run</em> the routing once computed, so another option would be to rent a large-memory Amazon machine for a day and have the extract processed there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '17, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-58971" class="comments-container">
<span id="59460"></span>
<div id="comment-59460" class="comment">
<div id="post-59460-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is unfortunate that you cannot extract on a machine that could actually run the program. But good idea with the outsourced processing. Thanks!</p>
</div>
<div id="comment-59460-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 08:13)</span> <span class="comment-user userinfo">wordli</span>
</div>
</div>
<span id="59469"></span>
<div id="comment-59469" class="comment">
<div id="post-59469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that older versions of OSRM have a smaller memory footprint: depending on the features you require, you may find that 4.9.1 fits your needs.</p>
</div>
<div id="comment-59469-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 15:41)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58971-form-container" class="comment-form-container">
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


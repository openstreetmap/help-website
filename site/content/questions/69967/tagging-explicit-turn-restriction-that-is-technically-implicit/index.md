+++
type = "question"
title = "Tagging explicit turn restriction that is technically implicit?"
description = '''Suppose you have this actually fairly common scenario: you have two one-way streets crossing each other. One is northbound, other is westbound. There is an &quot;explicit&quot; no right turn sign on the northbound street prohibiting an eastbound turn...which would be against the flow of traffic, which is the ...'''
date = "2019-07-10T17:12:00Z"
lastmod = "2019-07-13T22:36:00Z"
weight = 69967
keywords = [ "turn_restrictions", "implicit" ]
aliases = [ "/questions/69967" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging explicit turn restriction that is technically implicit?](/questions/69967/tagging-explicit-turn-restriction-that-is-technically-implicit)

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
<span id="post-69967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Suppose you have this actually fairly common scenario: you have two one-way streets crossing each other. One is northbound, other is westbound. There is an "explicit" no right turn sign on the northbound street prohibiting an eastbound turn...which would be against the flow of traffic, which is the "implicit" turn restriction.</p>
<p>Now I've been noticing people adding in the explicit turn restriction in and just leaving the relation unfinished because it's impossible to add the other elements with iD and possibly other editors due to the one way.</p>
<p>Should these turn restrictions be fleshed out somehow (perhaps add a sign saying so) or flushed out (remove the turn restriction in its entirety)? These unfinished turn restrictions both cause a KeepRight issue as well as cause a warning in mkgmap, so I've been deleting them due to the implicit nature of the restriction -- but should they still be marked, and how?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-implicit" rel="tag" title="see questions tagged &#39;implicit&#39;">implicit</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '19, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c86f4c99960b2c3ffdeb1698ba833b52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gpserror&#39;s gravatar image" />
<p><span>gpserror</span><br />
<span class="score" title="171 reputation points">171</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gpserror has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69967" class="comments-container">
<span id="69968"></span>
<div id="comment-69968" class="comment">
<div id="post-69968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've never seen an unfinished turn restriction. Do you have an example?</p>
</div>
<div id="comment-69968-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 17:19)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="69972"></span>
<div id="comment-69972" class="comment">
<div id="post-69972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Take a look at relation/restriction 8111223 (if I haven't fixed/deleted this restriction yet) - my guess is that there's a sign there and the original mapper tried to put the spirit of the sign in, but could get the rest of the relation in.)</p>
<p>Some others to look at: 6915842 9129946 7157302 -- again caveat that I haven't fixed them. Since there are thousands of these in the USA alone, this would take effort to fix them.</p>
</div>
<div id="comment-69972-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 17:52)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="69975"></span>
<div id="comment-69975" class="comment">
<div id="post-69975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The history of those relations shows that each one was a complete turn restriction relation initially, but that ways have since been removed from the relation. This looks simply like contributors introducing errors while editing existing data, not faulty mapping from the start or an editor issue.</p>
</div>
<div id="comment-69975-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 18:54)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="69976"></span>
<div id="comment-69976" class="comment">
<div id="post-69976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah interesting. In any case they still need to be fixed but unsure what's the best way to proceed. Seems like some editors have better protections against breakage.</p>
</div>
<div id="comment-69976-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 19:21)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="70048"></span>
<div id="comment-70048" class="comment">
<div id="post-70048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's a restriction ID with no history (no u-turn): 8385537 But yes, it looks like a lot of restrictions are broken due to moving roads around.</p>
<p>Sigh... some of these restriction relations are harder to fix than I thought. Back to the drawing board...</p>
</div>
<div id="comment-70048-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 18:29)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="70055"></span>
<div id="comment-70055" class="comment not_top_scorer">
<div id="post-70055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Something has gone terribly wrong there. A valid turn restriction at that intersection exists with <a href="https://www.openstreetmap.org/relation/8385544">8385544</a>. Have a look at the corresponding changeset. There are more broken and valid relations in there.</p>
</div>
<div id="comment-70055-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 22:36)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-69967" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69967-form-container" class="comment-form-container">
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

<span id="69969"></span>

<div id="answer-container-69969" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69969-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If a turn restriction relation is broken and at the same time unnecessary I would delete it. But I would leave a changeset comment to the original mapper explaining the issue.</p>
<p>If the turn restriction is working and valid, just unnecessary I would leave it as is. We should try to avoid destroying other mappers' works even if we would do it differently ourselves.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '19, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69969" class="comments-container">
<span id="69971"></span>
<div id="comment-69971" class="comment">
<div id="post-69971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that seems to be what I've been doing and leaving an explicit detail in the changelog why I removed them - I was a bit concerned as, well, there IS a sign there and the original mapper was trying to reflect the spirit of the sign. I haven't removed redundant restrictions ("working and valid"), in fact I would not even know that they exist as I'm only touching restrictions causing mkgmap/KeepRight warnings :)</p>
<p>I guess the last case is if it's unknown if necessary (can't verify) and also broken. KeepRight flags these but there haven't been changes for many months. I see this a lot. I try to look at Mapillary to see if these are needed and try to correct it but sometimes there's just not enough information.</p>
<p>I suppose a red X (map note) is needed for these? I'm just afraid I'm duplicating flagging as KeepRight marks them as light blue already -- though not everyone looks at KeepRight.</p>
</div>
<div id="comment-69971-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 17:46)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
</div>
<div id="comment-tools-69969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69969-form-container" class="comment-form-container">
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


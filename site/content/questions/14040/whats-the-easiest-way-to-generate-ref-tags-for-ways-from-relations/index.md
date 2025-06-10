+++
type = "question"
title = "What&#x27;s the easiest way to generate ref= tags for ways from relations?"
description = '''I&#x27;m currently working through relations and verifying alignment of Oklahoma state highways. I&#x27;m wondering, after I get relations done, what&#x27;s the easiest way to generate the ref=* tags for ways based on the networks and refs that it belongs to? For example, if a highway is a member of a relation wit...'''
date = "2012-07-06T17:23:00Z"
lastmod = "2012-07-07T02:15:00Z"
weight = 14040
keywords = [ "relations", "tagging" ]
aliases = [ "/questions/14040" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What's the easiest way to generate ref= tags for ways from relations?](/questions/14040/whats-the-easiest-way-to-generate-ref-tags-for-ways-from-relations)

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
<span id="post-14040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14040-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently working through relations and verifying alignment of Oklahoma state highways. I'm wondering, after I get relations done, what's the easiest way to generate the ref=* tags for ways based on the networks and refs that it belongs to? For example, if a highway is a member of a relation with (network=US:OK, ref=1) and another with (network=US, ref=270), the way should get ref=OK 1; US 270.</p>
<p>It seems a bulk change would be best once relations are completed and verified, but what would be the best way to accomplish that task?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '12, 17:23</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-14040" class="comments-container">
<span id="14042"></span>
<div id="comment-14042" class="comment">
<div id="post-14042-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Why does the way need a ref tag, if the refs are already in the relations?</p>
</div>
<div id="comment-14042-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 17:38)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="14051"></span>
<div id="comment-14051" class="comment">
<div id="post-14051-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>This question gets downvotes for, I assume, proposing a method that is presumed to be wrong (see Frederik's answer). Down- and upvotes on a question should be solely on the technical merits of the question itself (is it well-formed? Not a duplicate? Not solliciting opinions?) and not on the methods suggested. For that, we have discussion forums and mailing lists. This is, the way I see it, a site for practical, answerable questions based on reasonably scoped real-world problems. We should not clutter it by opinionating.</p>
</div>
<div id="comment-14051-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 20:55)</span> <span class="comment-user userinfo">mvexel</span>
</div>
</div>
</div>
<div id="comment-tools-14040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14040-form-container" class="comment-form-container">
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

<span id="14041"></span>

<div id="answer-container-14041" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14041-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The way should certainly not get a ref tag based on the relation, and <strong>most</strong> certainly not by way of a bulk change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '12, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14041" class="comments-container">
<span id="14044"></span>
<div id="comment-14044" class="comment">
<div id="post-14044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Though if the relations are accurate, what's the problem with generating the refs from the relations?</p>
</div>
<div id="comment-14044-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 19:04)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="14045"></span>
<div id="comment-14045" class="comment">
<div id="post-14045-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Problem is that you are generating data duplication with it. If the ref information already exists on relations then it should not exist on the ways any more.</p>
</div>
<div id="comment-14045-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 19:09)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="14048"></span>
<div id="comment-14048" class="comment">
<div id="post-14048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's kind of what I was thinking, too. However, in practice, since Mapnik doesn't render relation references, people will add them anyway. In places like Oklahoma, where duplex routes of 4 different refs aren't uncommon, an incomplete ref isn't the answer.</p>
</div>
<div id="comment-14048-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 19:30)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="14049"></span>
<div id="comment-14049" class="comment">
<div id="post-14049-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>If the standard mapnik rendering does not render ref tags from relations then it is a rendering issue. If you do a search on trac then you can find a ticket about it: <a href="https://trac.openstreetmap.org/ticket/2610">https://trac.openstreetmap.org/ticket/2610</a> . Sadly it is still waiting implementation. But it does not mean that in the meantime data duplication should be generated because of rendering shortcomings.</p>
</div>
<div id="comment-14049-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 19:59)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="14050"></span>
<div id="comment-14050" class="comment">
<div id="post-14050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>True enough, but it is exploiting a human shortcoming in the meantime.</p>
</div>
<div id="comment-14050-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 20:15)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="14053"></span>
<div id="comment-14053" class="comment not_top_scorer">
<div id="post-14053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While I agree with the sentiment that it is duplication of data and would rather not do so, this is the only reasonable way to do it right now to get anything sensible in both rendering and routing data. Mapnik, MapQuest, OSRM, YOURS, cloudmade... they all use ref=* on ways. And as pointed out by the trac ticket above, it has been this way for years which means that by now, tagging the highway ref on ways is a very well established standard in the US, like it or not. I would be happy to do a mass edit to remove them... when enough tools support route relations.</p>
</div>
<div id="comment-14053-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 23:12)</span> <span class="comment-user userinfo">ToeBee</span>
</div>
</div>
<span id="14056"></span>
<div id="comment-14056" class="comment not_top_scorer">
<div id="post-14056-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is MapQuest actively maintaining and accepting it's own mapnik styles on Github? I'd be interested in fixing the problem for the base mapnik and MQ mapnik if possible.</p>
</div>
<div id="comment-14056-info" class="comment-info">
<span class="comment-age">(07 Jul '12, 02:15)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-14041" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-14041-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14046"></span>

<div id="answer-container-14046" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14046-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure why you'd want to copy relation attributes to constituent ways within the data itself. If it's for use on a Garmin map, have a look <a href="https://wiki.openstreetmap.org/wiki/Mkgmap/help/style_rules">here</a> at the use of "apply" to acheive the result of having the way labelled with relation refs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '12, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-14046" class="comments-container">
<span id="14055"></span>
<div id="comment-14055" class="comment">
<div id="post-14055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Largely to head off some tag fiddling people do to make route refs render otherwise. Though I'd be interested if Lambertus is generating garmin tiles that take refs from relations overriding refs on ways.</p>
</div>
<div id="comment-14055-info" class="comment-info">
<span class="comment-age">(07 Jul '12, 02:14)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-14046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14046-form-container" class="comment-form-container">
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


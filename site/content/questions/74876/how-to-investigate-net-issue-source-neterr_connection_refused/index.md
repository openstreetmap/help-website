+++
type = "question"
title = "how to investigate net issue source ?? net::ERR_CONNECTION_REFUSED"
description = '''Hi, during my app development I encounter issue. so far everything was up and running and now I got net::ERR_CONNECTION_REFUSED. How can I investigate the source of problem?? was this because of to much queries so I was blocked ?'''
date = "2020-05-18T15:40:00Z"
lastmod = "2020-05-18T17:07:00Z"
weight = 74876
keywords = [ "provider" ]
aliases = [ "/questions/74876" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to investigate net issue source ?? net::ERR_CONNECTION_REFUSED](/questions/74876/how-to-investigate-net-issue-source-neterr_connection_refused)

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
<span id="post-74876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74876-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, during my app development I encounter issue. so far everything was up and running and now I got net::ERR_CONNECTION_REFUSED. How can I investigate the source of problem?? was this because of to much queries so I was blocked ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-provider" rel="tag" title="see questions tagged &#39;provider&#39;">provider</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 May '20, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/12479e1ab6f16fa4e5a96ca52bca909b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kacpero&#39;s gravatar image" />
<p><span>kacpero</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kacpero has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74876" class="comments-container">
<span id="74877"></span>
<div id="comment-74877" class="comment">
<div id="post-74877-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Well how many queries did you make, and to what service?</p>
</div>
<div id="comment-74877-info" class="comment-info">
<span class="comment-age">(18 May '20, 15:47)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="74878"></span>
<div id="comment-74878" class="comment">
<div id="post-74878-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's probable, but please share the offending URLs so we can know what you are talking about. Regards.</p>
</div>
<div id="comment-74878-info" class="comment-info">
<span class="comment-age">(18 May '20, 15:48)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="74880"></span>
<div id="comment-74880" class="comment">
<div id="post-74880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi the strange thing about this is that only my computer failing in this connection request. It's localhost. never deployed yet. Its about OpeenStreetMapProvider</p>
</div>
<div id="comment-74880-info" class="comment-info">
<span class="comment-age">(18 May '20, 16:05)</span> <span class="comment-user userinfo">kacpero</span>
</div>
</div>
<span id="74881"></span>
<div id="comment-74881" class="comment">
<div id="post-74881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for not specify my query the thing is about nominate opeenStreetMapProvider</p>
</div>
<div id="comment-74881-info" class="comment-info">
<span class="comment-age">(18 May '20, 16:08)</span> <span class="comment-user userinfo">kacpero</span>
</div>
</div>
<span id="74883"></span>
<div id="comment-74883" class="comment">
<div id="post-74883-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here is the usage policy for Nominatim: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a></p>
</div>
<div id="comment-74883-info" class="comment-info">
<span class="comment-age">(18 May '20, 16:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="74884"></span>
<div id="comment-74884" class="comment not_top_scorer">
<div id="post-74884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes I know and still as only developer doubt I broke usage policy so my question is how can I investigate the issue in case of usage breaking is there a chance to unblock me? How can I check whether I am breaking or not the usage policy so in the future my production version would not encounter such issue. In other hand are you familiar with any alternative to openStreetMapProvider so I can use withaout limitations? Thank you in advanced. Sorry for this is I am realy beginner programmer.</p>
</div>
<div id="comment-74884-info" class="comment-info">
<span class="comment-age">(18 May '20, 16:39)</span> <span class="comment-user userinfo">kacpero</span>
</div>
</div>
</div>
<div id="comment-tools-74876" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-74876-form-container" class="comment-form-container">
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

<span id="74885"></span>

<div id="answer-container-74885" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74885-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-74885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you comply with "Provide a valid HTTP Referer or User-Agent identifying the application" ? Easily overlooked. Although the 1 request per second limit is easy to trigger by accident !</p>
<p>There's no way of checking blocks that I know of. Most of this things are managed by volunteers, so it is usually crude.</p>
<p>You probably only have to wait and see if it's unblocked.</p>
<p>For alternatives, on the previously mentioned links, it links to this list : <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers">https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers</a></p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '20, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74885" class="comments-container">
<span id="74886"></span>
<div id="comment-74886" class="comment">
<div id="post-74886-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much for your answer :) really appreciate and of course I overlooked your first point :p</p>
</div>
<div id="comment-74886-info" class="comment-info">
<span class="comment-age">(18 May '20, 17:07)</span> <span class="comment-user userinfo">kacpero</span>
</div>
</div>
</div>
<div id="comment-tools-74885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74885-form-container" class="comment-form-container">
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


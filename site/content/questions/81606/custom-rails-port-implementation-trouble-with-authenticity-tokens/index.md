+++
type = "question"
title = "custom Rails Port implementation, trouble with Authenticity Tokens"
description = '''Is there anyone in this channel who can talk to me about the Rails Port&#x27;s &quot;authenticity token&quot; system? I have been implementing a new, customized Rails Port instance for https://opengeofiction.net/ . It&#x27;s working well but I am having nightmare problems with two things:  Frequent errors for users: &quot;A...'''
date = "2021-09-02T18:26:00Z"
lastmod = "2021-09-04T17:44:00Z"
weight = 81606
keywords = [ "rubyonrails" ]
aliases = [ "/questions/81606" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [custom Rails Port implementation, trouble with Authenticity Tokens](/questions/81606/custom-rails-port-implementation-trouble-with-authenticity-tokens)

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
<span id="post-81606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81606-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there anyone in this channel who can talk to me about the Rails Port's "authenticity token" system?</p>
<p>I have been implementing a new, customized Rails Port instance for <a href="https://opengeofiction.net/">https://opengeofiction.net/</a> . It's working well but I am having nightmare problems with two things:</p>
<ul>
<li>Frequent errors for users: "ActionController::InvalidAuthenticityToken"</li>
<li>Frequently users are forcibly logged off whenever they change pages (i.e. Diaries to map, map to iD, etc.)</li>
</ul>
<p>Is there anyone who can give me insights into what might be going wrong.</p>
<p>I am not a Ruby on Rails developer or even particularly comfortable with the environment. I have a background in Database admin and design and I am comfortable with most aspects of Linux sysadmin.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rubyonrails" rel="tag" title="see questions tagged &#39;rubyonrails&#39;">rubyonrails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '21, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/1a385e5141831c1926b4254ecc620ea3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luciano%20AK&#39;s gravatar image" />
<p><span>Luciano AK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luciano AK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81606" class="comments-container">
<span id="81609"></span>
<div id="comment-81609" class="comment">
<div id="post-81609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain the changes you have made to the "original", or do you have your version on GitHub somewhere?</p>
</div>
<div id="comment-81609-info" class="comment-info">
<span class="comment-age">(03 Sep '21, 09:36)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="81612"></span>
<div id="comment-81612" class="comment">
<div id="post-81612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik</a> - I'm sorry we don't have it on github. It's all kind of experimental. In the long run, we hope to formally "fork" openstreetmap-website and post our changes, but we're not there right now.</p>
<p>Meanwhile, the site is up and seems to be working. We've let in a limited number of users and we're doing testing. Not going to claim victory, yet, but the Authenticity Token errors appear to have gone away. We did a bunch of google-fu and dug up what seemed to have worked. I promise I'll post what we did once I'm confident it worked.</p>
<p>You're free to browse the website:</p>
<p><a href="https://opengeofiction.net">https://opengeofiction.net</a></p>
<p>Anyway thank you so much for taking the time to respond.</p>
</div>
<div id="comment-81612-info" class="comment-info">
<span class="comment-age">(03 Sep '21, 19:33)</span> <span class="comment-user userinfo">Luciano AK</span>
</div>
</div>
</div>
<div id="comment-tools-81606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81606-form-container" class="comment-form-container">
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

<span id="81615"></span>

<div id="answer-container-81615" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81615-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, thank you to my one responder, for their suggestion.</p>
<p>Apparently, the openstreetmap-website ("rails port") expects that a production instance will have a tool called <em>memcache</em> installed. It was another member of our team who figured this out, so I don't have the details, but I think that's enough of a hint if someone finds this question in the future and is trying to solve the issue.</p>
<p>Although we are still running the "rails port" as a development instance (rather than production), we are doing so as a de facto production instance, with 100's of active users.</p>
<p>This level of deployment requires <em>memcache</em> to manage the authenticity tokens, I guess.</p>
<p>If I get more details from my colleague about specific steps he took, I'll amend this answer.</p>
<p>Meanwhile, our site is up and running quite well, now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '21, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/1a385e5141831c1926b4254ecc620ea3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luciano%20AK&#39;s gravatar image" />
<p><span>Luciano AK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luciano AK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81615" class="comments-container">
&#10;</div>
<div id="comment-tools-81615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81615-form-container" class="comment-form-container">
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


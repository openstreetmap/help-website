+++
type = "question"
title = "Error RStudio peer certificate"
description = '''Hi, I cannot use OSM to getbb() in RStudio.  The error response is: Peer certificate cannot be authenticated with given CA certificates: [nominatim.openstreetmap.org] SSL certificate problem: certificate has expired Backtrace:  1. osmdata::getbb(&quot;Montevideo, Uruguay&quot;)  2. osmdata:::get_nominatim_que...'''
date = "2023-08-18T21:59:00Z"
lastmod = "2023-08-19T13:18:00Z"
weight = 87705
keywords = [ "peer", "certificate", "error" ]
aliases = [ "/questions/87705" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error RStudio peer certificate](/questions/87705/error-rstudio-peer-certificate)

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
<span id="post-87705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I cannot use OSM to getbb() in RStudio. The error response is:</p>
<pre><code>Peer certificate cannot be authenticated with given CA certificates: [nominatim.openstreetmap.org] SSL certificate problem: certificate has expired
Backtrace:
 1. osmdata::getbb(&quot;Montevideo, Uruguay&quot;)
 2. osmdata:::get_nominatim_query(...)
 3. httr2::req_perform(req)
 4. base::tryCatch(...)
 5. base (local) tryCatchList(expr, classes, parentenv, handlers)
 6. base (local) tryCatchOne(expr, names, parentenv, handlers[[1L]])
 7. value[[3L]](cond)</code></pre>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-peer" rel="tag" title="see questions tagged &#39;peer&#39;">peer</span> <span class="post-tag tag-link-certificate" rel="tag" title="see questions tagged &#39;certificate&#39;">certificate</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '23, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0ba5918672ad87e99f3443f33d11fdd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="virginia_recagno&#39;s gravatar image" />
<p><span>virginia_rec...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="virginia_recagno has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '23, 22:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-87705" class="comments-container">
<span id="87706"></span>
<div id="comment-87706" class="comment">
<div id="post-87706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What's the URL for which the certificate has expired? It isn't the "nominatim.openstreetmap.org" that I can see from where I am, which is:</p>
<pre><code>Name:   longma.nominatim.openstreetmap.org
Address: 184.104.226.109
Name:   longma.nominatim.openstreetmap.org
Address: 2001:470:1:b3b::d</code></pre>
</div>
<div id="comment-87706-info" class="comment-info">
<span class="comment-age">(18 Aug '23, 22:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87707"></span>
<div id="comment-87707" class="comment">
<div id="post-87707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I dont know. Im a Mac User and I've been using OSM just fine, but now I can't. It takes many minutes to load and finally just says:</p>
<p>"Peer certificate cannot be authenticated with given CA certificates: [nominatim.openstreetmap.org] SSL certificate problem: certificate has expired "</p>
</div>
<div id="comment-87707-info" class="comment-info">
<span class="comment-age">(18 Aug '23, 22:20)</span> <span class="comment-user userinfo">virginia_rec...</span>
</div>
</div>
<span id="87708"></span>
<div id="comment-87708" class="comment">
<div id="post-87708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In a web browser, try and browse to nominatim.openstreetmap.org and follow the instructions at <a href="https://discussions.apple.com/thread/250173734">https://discussions.apple.com/thread/250173734</a> . What does it say?</p>
<p>What is the date on your Mac set to? Is it correct?</p>
<p>Can you try and browse to nominatim.openstreetmap.org on a non-Apple computer and tap on the padlock icon in the URL bar there?</p>
</div>
<div id="comment-87708-info" class="comment-info">
<span class="comment-age">(18 Aug '23, 22:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87710"></span>
<div id="comment-87710" class="comment">
<div id="post-87710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your response. Its not a browser issue... If I follow your instructions, it says: "Safe connection" "Conection verifyed by an emisor not recognized by Mozilla. My date is set just fine. And I been working with OSM y in RSTUDIO (osmr package) just fine until this came up.</p>
</div>
<div id="comment-87710-info" class="comment-info">
<span class="comment-age">(19 Aug '23, 13:18)</span> <span class="comment-user userinfo">virginia_rec...</span>
</div>
</div>
</div>
<div id="comment-tools-87705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


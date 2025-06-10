+++
type = "question"
title = "Authorizing for the API - Good practices"
description = '''I want to use the OSM API in my C# application to edit data coming from my app. I was just wondering about authentication. I know the API has both basic http authentication and OAuth. Which one is the better option? Since you have to input your username+password for basic http authentation, won&#x27;t th...'''
date = "2016-10-11T15:33:00Z"
lastmod = "2016-10-12T09:55:00Z"
weight = 52479
keywords = [ "oauth", "basic_authentication" ]
aliases = [ "/questions/52479" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Authorizing for the API - Good practices](/questions/52479/authorizing-for-the-api-good-practices)

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
<span id="post-52479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52479-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to use the OSM API in my C# application to edit data coming from my app. I was just wondering about authentication. I know the API has both basic http authentication and OAuth. Which one is the better option? Since you have to input your username+password for basic http authentation, won't this be insecure?</p>
<p>And when using OAuth, how will this work exactly? You have to make a request of some sort and it will return a token which you can use to sign requests with? I'm not very familiar with OAuth, so any help would be appreciated on this.</p>
<p>For clarification: My app will have a list of restaurants coming from OSM. When a restaurant owner edits it's profile page (E.g. it's address), I will have to update this to OSM (According to the policies).</p>
<p>Yes, I'm fairly new to using APIs and brand new to using the OSM API, so any help would be greatly appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span> <span class="post-tag tag-link-basic_authentication" rel="tag" title="see questions tagged &#39;basic_authentication&#39;">basic_authentication</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '16, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/63cd527e1907dc104991b729f3d74a15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BasBouwhuis&#39;s gravatar image" />
<p><span>BasBouwhuis</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BasBouwhuis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52479" class="comments-container">
&#10;</div>
<div id="comment-tools-52479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52479-form-container" class="comment-form-container">
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

<span id="52484"></span>

<div id="answer-container-52484" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52484-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BasBouwhuis has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You definitely want to use OAuth this avoids storing login/password on the device completely.</p>
<p>Your app first needs to get a consumer key and a consumer secret, see <a href="https://www.openstreetmap.org/user/XXXXX/oauth_clients/new">https://www.openstreetmap.org/user/XXXXX/oauth_clients/new</a> This is a one time action done by the developer of the app.</p>
<p>For the rest see for example <a href="https://marktrapp.com/blog/2009/09/17/oauth-dummies/">https://marktrapp.com/blog/2009/09/17/oauth-dummies/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '16, 23:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '16, 23:29</strong> </span></p>
</div>
</div>
<div id="comments-container-52484" class="comments-container">
<span id="52489"></span>
<div id="comment-52489" class="comment">
<div id="post-52489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Awesome, thanks! Quick question, how long are the request token and access token valid?</p>
<p>Edit: The API isn't supplying me with a oauth_verifier token when I grant access to the user.</p>
<p>I have gotten the oauth_token and oauth_token_secret when sending a request to the request token url.</p>
<p>I have also authorized this, by making a request to this url: <a href="http://api06.dev.openstreetmap.org/oauth/authorize.">http://api06.dev.openstreetmap.org/oauth/authorize.</a> When I didn't have a callback url, it would just say it has granted me access. When I did provide a callback url, it would just go to the url with the already provided OAuth token, but nothing else.</p>
<p>When I made a request to <a href="http://api06.dev.openstreetmap.org/oauth/access_token">http://api06.dev.openstreetmap.org/oauth/access_token</a> with the tokens, I got an 401 Unauthorized error code.</p>
<p>What am I doing wrong?</p>
</div>
<div id="comment-52489-info" class="comment-info">
<span class="comment-age">(12 Oct '16, 08:19)</span> <span class="comment-user userinfo">BasBouwhuis</span>
</div>
</div>
<span id="52490"></span>
<div id="comment-52490" class="comment">
<div id="post-52490-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm fairly sure your base URL is wrong for the dev instance, IMHO it should be <a href="http://master.apis.dev.openstreetmap.org/">http://master.apis.dev.openstreetmap.org/</a> but I might be mistaken.</p>
<p>You are probably better off asking on the #osm-dev IRC channel (you may need to wait a while for an answer).</p>
</div>
<div id="comment-52490-info" class="comment-info">
<span class="comment-age">(12 Oct '16, 09:46)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="52491"></span>
<div id="comment-52491" class="comment">
<div id="post-52491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I read somewhere I should test my application against that url before using the real OSM url, it does work for everything but the access_token.</p>
<p>I'll ask around for getting the access_token, once again thank you very much!</p>
</div>
<div id="comment-52491-info" class="comment-info">
<span class="comment-age">(12 Oct '16, 09:55)</span> <span class="comment-user userinfo">BasBouwhuis</span>
</div>
</div>
</div>
<div id="comment-tools-52484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52484-form-container" class="comment-form-container">
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


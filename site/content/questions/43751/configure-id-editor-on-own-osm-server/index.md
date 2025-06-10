+++
type = "question"
title = "configure iD editor on own osm server"
description = '''Hi, I created my own osm server and I appended some data. I would like to use iD editor to change something, but I&#x27;m not able to do it. When I press edit tab in the web I receive the application error 500. In the following the lines in the production.log: I, [2015-06-24T09:16:14.256607 #14679] INFO ...'''
date = "2015-06-24T10:43:00Z"
lastmod = "2015-07-06T14:52:00Z"
weight = 43751
keywords = [ "ideditor" ]
aliases = [ "/questions/43751" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [configure iD editor on own osm server](/questions/43751/configure-id-editor-on-own-osm-server)

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
<span id="post-43751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43751-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I created my own osm server and I appended some data. I would like to use iD editor to change something, but I'm not able to do it. When I press edit tab in the web I receive the application error 500. In the following the lines in the production.log:</p>
<p>I, [2015-06-24T09:16:14.256607 #14679] INFO -- : Rendered site/id.html.erb (182.3ms) I, [2015-06-24T09:16:14.256943 #14679] INFO -- : Completed 500 Internal Server Error in 189ms (ActiveRecord: 3.1ms) F, [2015-06-24T09:16:14.258915 #14679] FATAL -- : ActionView::Template::Error (undefined method <code>access_token_for_user' for nil:NilClass): 28: .locale("&lt;%= locale %&gt;", "&lt;%= asset_path("iD/locales/#{locale}.json") %&gt;") 29: .preauth({ 30: &lt;% token = </code><a href="http://help.openstreetmap.org/users/6901/user"><code>@user</code></a><code>.access_token(ID_KEY) %&gt; 31: url: "&lt;%= request.protocol + request.host_with_port %&gt;", 32: oauth_consumer_key: "&lt;%= token.client_application.key %&gt;", 33: oauth_secret: "&lt;%= token.client_application.secret %&gt;", 34: oauth_token: "&lt;%= token.token %&gt;", app/models/user.rb:239:in</code>access_token' app/views/site/id.html.erb:31:in <code>_app_views_site_id_html_erb___1011942628133712304_61090920' app/controllers/site_controller.rb:118:in</code>id' config/initializers/cors.rb:9:in `call'</p>
<p>I think the problem is related to user_tokens and client_applications table. I do not know how to fill them. Could you help me?</p>
<p>Thank you, Laura</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '15, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a82a93c2ba40de678ebedb9a97b66e31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Laura&#39;s gravatar image" />
<p><span>Laura</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Laura has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jul '15, 22:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-43751" class="comments-container">
&#10;</div>
<div id="comment-tools-43751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43751-form-container" class="comment-form-container">
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

<span id="43808"></span>

<div id="answer-container-43808" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43808-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you are getting this error because <a href="http://help.openstreetmap.org/users/6901/user"></a><a href="http://help.openstreetmap.org/users/6901/user"></a><a href="http://help.openstreetmap.org/users/6901/user"><code>@user</code></a></a></a> is nil on line 30. The rails site will redirect to the login page if there is no <a href="http://help.openstreetmap.org/users/6901/user"></a><a href="http://help.openstreetmap.org/users/6901/user"></a><a href="http://help.openstreetmap.org/users/6901/user"><code>@user</code></a></a></a>, so you probably changed some code elsewhere that performs the redirect.</p>
<p>Alternatively, on your site you could choose to allow un-loggedin users to use iD by wrapping the <code>preauth</code> code in a condition that will just not include it if <a href="http://help.openstreetmap.org/users/6901/user"></a><a href="http://help.openstreetmap.org/users/6901/user"></a><a href="http://help.openstreetmap.org/users/6901/user"><code>@user</code></a></a></a> is nil. iD will work fine without <code>preauth</code>, but will prompt the user to authenticate when they attempt to save something.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '15, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/5372740989fdca18458f194a285fcb3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhousel&#39;s gravatar image" />
<p><span>bhousel</span><br />
<span class="score" title="2089 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhousel has 13 accepted answers">38%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '15, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-43808" class="comments-container">
<span id="44006"></span>
<div id="comment-44006" class="comment">
<div id="post-44006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Thank you for your answer. I have not changed the server code, but probably there are some problems in some database tables. I was wondering if someone can help me in understanding what I have to write in the user_tokens and client_applications table for a particular user. Thank you, Laura</p>
</div>
<div id="comment-44006-info" class="comment-info">
<span class="comment-age">(06 Jul '15, 14:52)</span> <span class="comment-user userinfo">Laura</span>
</div>
</div>
</div>
<div id="comment-tools-43808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43808-form-container" class="comment-form-container">
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


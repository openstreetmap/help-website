+++
type = "question"
title = "customizing website from rails port"
description = '''Hi. I did setup sucessfully a Openstreetmap Website following https://github.com/openstreetmap/openstreetmap-website/issues and now I want to customize the website, like changing the background colors, fonts, texts and so on, but I don&#x27;t know how to do it. Looking in the folders I didn&#x27;t found an In...'''
date = "2019-07-30T15:03:00Z"
lastmod = "2019-09-07T13:06:00Z"
weight = 70240
keywords = [ "website", "railsport" ]
aliases = [ "/questions/70240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [customizing website from rails port](/questions/70240/customizing-website-from-rails-port)

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
<span id="post-70240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70240-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I did setup sucessfully a Openstreetmap Website following <a href="https://github.com/openstreetmap/openstreetmap-website/issues">https://github.com/openstreetmap/openstreetmap-website/issues</a> and now I want to customize the website, like changing the background colors, fonts, texts and so on, but I don't know how to do it. Looking in the folders I didn't found an Index.html like any other website have. So my question is: How can I edit my OSM Website?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '19, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70240" class="comments-container">
&#10;</div>
<div id="comment-tools-70240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70240-form-container" class="comment-form-container">
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

<span id="70246"></span>

<div id="answer-container-70246" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70246-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://github.com/openstreetmap/openstreetmap-website">openstreetmap-website</a> codebase is built on <a href="https://rubyonrails.org/">Ruby on Rails</a> and follows all the normal conventions from that framework. So to customise your copy of the site:</p>
<ul>
<li>The CSS files are available in <a href="https://github.com/openstreetmap/openstreetmap-website/tree/master/app/assets/stylesheets"><code>app/assets/stylesheets/</code></a></li>
<li>HTML code for the basic page layouts is in <a href="https://github.com/openstreetmap/openstreetmap-website/tree/master/app/views/layouts"><code>app/views/layouts/</code></a></li>
<li>HTML code for specific pages is in the other directories in <a href="https://github.com/openstreetmap/openstreetmap-website/tree/master/app/views"><code>app/views/</code></a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '19, 07:43</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-70246" class="comments-container">
<span id="70530"></span>
<div id="comment-70530" class="comment">
<div id="post-70530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for the late answer. I'm trying to do some changes but without sucess. I want to change the image logo at the main page in the top left part. I changed to osm_logo files at openstreetmap-website/app/assets but it still the old image. Which file I need to change?</p>
</div>
<div id="comment-70530-info" class="comment-info">
<span class="comment-age">(27 Aug '19, 00:58)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="70673"></span>
<div id="comment-70673" class="comment">
<div id="post-70673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What if I would like to change the style of a specific feature (highways for example)?</p>
</div>
<div id="comment-70673-info" class="comment-info">
<span class="comment-age">(07 Sep '19, 13:06)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-70246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70246-form-container" class="comment-form-container">
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


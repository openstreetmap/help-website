+++
type = "question"
title = "[Nominatim]: The underlying connection was closed"
description = '''I have been using nominatim for reverse geo-coding purpose. I send so many asynchronous requests to retrieve geo locations based on latitude and longitude.  I am using nominatim version 2.4.  And because of that I receive an error saying:  The underlying connection was closed: A connection that was ...'''
date = "2015-09-10T05:46:00Z"
lastmod = "2015-09-14T08:03:00Z"
weight = 45153
keywords = [ "c#", "asp.net", "nominatim" ]
aliases = [ "/questions/45153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Nominatim\]: The underlying connection was closed](/questions/45153/nominatim-the-underlying-connection-was-closed)

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
<span id="post-45153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45153-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been using nominatim for reverse geo-coding purpose. I send so many asynchronous requests to retrieve geo locations based on latitude and longitude.</p>
<p>I am using nominatim <code>version 2.4</code>.</p>
<p>And because of that I receive an error saying:</p>
<p><strong>The underlying connection was closed: A connection that was expected to be kept alive was closed by the server. at System.Net.HttpWebRequest.GetResponse()</strong></p>
<p>So I would like to know that whether is there any solution to get rid of it ? Is there any configuration for maximum connection request ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-asp.net" rel="tag" title="see questions tagged &#39;asp.net&#39;">asp.net</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '15, 05:46</strong></p>
<img src="https://secure.gravatar.com/avatar/5847213073703288add351b13ecf084c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SpiderCode&#39;s gravatar image" />
<p><span>SpiderCode</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SpiderCode has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45153" class="comments-container">
<span id="45169"></span>
<div id="comment-45169" class="comment">
<div id="post-45169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>are you running your own instance of Nominatim ? Or are you using nominatim.openstreetmap.org ? In that latter case, you have to be aware that there is a limit on the number of request you can make. It is not meant for commercial purposes, and you should install your own instance of Nominatim in that case.</p>
</div>
<div id="comment-45169-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 14:53)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="45170"></span>
<div id="comment-45170" class="comment">
<div id="post-45170-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am running my own Nominatim instance</p>
</div>
<div id="comment-45170-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 14:56)</span> <span class="comment-user userinfo">SpiderCode</span>
</div>
</div>
<span id="45231"></span>
<div id="comment-45231" class="comment">
<div id="post-45231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5390/escada">@escada</a> : Is there any possible way to do this ?</p>
</div>
<div id="comment-45231-info" class="comment-info">
<span class="comment-age">(14 Sep '15, 07:31)</span> <span class="comment-user userinfo">SpiderCode</span>
</div>
</div>
<span id="45232"></span>
<div id="comment-45232" class="comment">
<div id="post-45232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I have never installed Nominatim myself. I was just asking additional questions because it was not clear to me whether you were running your own instance or not</p>
</div>
<div id="comment-45232-info" class="comment-info">
<span class="comment-age">(14 Sep '15, 08:03)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-45153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45153-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


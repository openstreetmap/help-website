+++
type = "question"
title = "Web API test results in ERROR 404: Not Found."
description = '''Hi all, I&#x27;ve installed OSM3S and it works fine in static usage. I&#x27;ve then set up the Web API following the instructions in the Overpass API installation wiki and everything seemed to work properly but when I run the test (with the dispatcher running in the background): wget --output-document=test.xm...'''
date = "2019-05-06T17:47:00Z"
lastmod = "2019-05-06T17:47:00Z"
weight = 69108
keywords = [ "http_status_code_404" ]
aliases = [ "/questions/69108" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Web API test results in ERROR 404: Not Found.](/questions/69108/web-api-test-results-in-error-404-not-found)

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
<span id="post-69108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69108-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I've installed OSM3S and it works fine in static usage.</p>
<p>I've then set up the Web API following the instructions in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Setting_up_the_Web_API">Overpass API installation wiki</a> and everything seemed to work properly but when I run the test (with the dispatcher running in the background):</p>
<p><code>wget --output-document=test.xml </code><a href="http://localhost/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E"><code>http://localhost/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E</code></a></p>
<p>I get a 404 response:</p>
<p><code>--2019-05-03 16:49:32-- </code><a href="http://localhost/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E"><code>http://localhost/api/interpreter?data=%3Cprint%20mode=%22body%22/%3E</code></a><code> Resolving localhost (localhost)... 127.0.0.1 Connecting to localhost (localhost)|127.0.0.1|:80... connected. HTTP request sent, awaiting response... 404 Not Found 2019-05-03 16:49:32 ERROR 404: Not Found.</code></p>
<p>Could please anyone point me to possible problems/solutions? I've double checked the paths in the apache configuration file and they are ok. It doesn't seem to be a permission problem either. Any suggestion is appreciated.</p>
<p>Many thanks,</p>
<p>Carlo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-http_status_code_404" rel="tag" title="see questions tagged &#39;http_status_code_404&#39;">http_status_code_404</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '19, 17:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a16bc8af34277c959cf839b99a594d7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlo_co&#39;s gravatar image" />
<p><span>carlo_co</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlo_co has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69108" class="comments-container">
&#10;</div>
<div id="comment-tools-69108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69108-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


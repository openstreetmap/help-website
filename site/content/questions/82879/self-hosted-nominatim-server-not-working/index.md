+++
type = "question"
title = "Self-hosted Nominatim Server not working"
description = '''Having recently set-up my own OSM server using the instructions at switch2osm.com I have been attempting to configure a nominatim server. I&#x27;m running Ubuntu 20.04 and followed the instructions here: https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/ The directory pointed to wit...'''
date = "2021-12-20T16:00:00Z"
lastmod = "2021-12-20T16:09:00Z"
weight = 82879
keywords = [ "nominatim" ]
aliases = [ "/questions/82879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Self-hosted Nominatim Server not working](/questions/82879/self-hosted-nominatim-server-not-working)

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
<span id="post-82879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Having recently set-up my own OSM server using the instructions at switch2osm.com I have been attempting to configure a nominatim server.</p>
<p>I'm running Ubuntu 20.04 and followed the instructions here: <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/</a></p>
<p>The directory pointed to within Apache2 nominatim.conf file exists (svr/nominatim/build/website) and permissions are set correctly - if I put a basic html or php file in the directory I can access either. However, the installer didn't put search.php, status.php etc in the same location. Copying the versions files that the installer did create hasn't worked.</p>
<p>The installation is otherwise sound - I've imported data and accessing nominatim via the test server (<code>nominatim serve</code>) works for forward and reverse look-ups.</p>
<p>Any suggestions?</p>
<p>DD.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '21, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a56f2b9adffd6d99321d04f8d7f343de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DephiDinosaur&#39;s gravatar image" />
<p><span>DephiDinosaur</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DephiDinosaur has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82879" class="comments-container">
&#10;</div>
<div id="comment-tools-82879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82879-form-container" class="comment-form-container">
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

<span id="82880"></span>

<div id="answer-container-82880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82880-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As the installation page says "The webserver should serve the php scripts from the website directory of your project directory." (not the build directory). For example <code>$USERHOME/nominatim-project/website</code></p>
<p>If the *.php files are not in the project directory's 'website' sub-directory yet, try running "<code>nominatim refresh --website</code>" from within the project directory. That copies the necessary files from the build directory to the project directory (it also changes the first lines of each file slightly).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '21, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '21, 16:15</strong> </span></p>
</div>
</div>
<div id="comments-container-82880" class="comments-container">
&#10;</div>
<div id="comment-tools-82880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82880-form-container" class="comment-form-container">
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


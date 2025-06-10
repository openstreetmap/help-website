+++
type = "question"
title = "Installing Osmosis on OSX"
description = '''I am using Snow Leopard and am trying to use Osmosis, but it refuses to work with me. I get the error below whenever I try to just open Osmosis: Mac:osmosis-0.38 George$ java /Users/George/Downloads/osmosis-0.38/bin/osmosis  Exception in thread &quot;main&quot; java.lang.NoClassDefFoundError: /Users/George/Do...'''
date = "2011-02-20T09:17:00Z"
lastmod = "2011-02-21T21:17:00Z"
weight = 3214
keywords = [ "osx", "osmosis", "install" ]
aliases = [ "/questions/3214" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Installing Osmosis on OSX](/questions/3214/installing-osmosis-on-osx)

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
<span id="post-3214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3214-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using Snow Leopard and am trying to use Osmosis, but it refuses to work with me.</p>
<p>I get the error below whenever I try to just open Osmosis:</p>
<p>Mac:osmosis-0.38 George$ java /Users/George/Downloads/osmosis-0.38/bin/osmosis Exception in thread "main" java.lang.NoClassDefFoundError: /Users/George/Downloads/osmosis-0/38/bin/osmosis Caused by: java.lang.ClassNotFoundException: .Users.George.Downloads.osmosis-0.38.bin.osmosis at <a href="http://java.net">java.net</a>.URLClassLoader$1.run(URLClassLoader.java:202) at java.security.AccessController.doPrivileged(Native Method) at <a href="http://java.net">java.net</a>.URLClassLoader.findClass(URLClassLoader.java:190) at java.lang.ClassLoader.loadClass(ClassLoader.java:307) at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:301) at java.lang.ClassLoader.loadClass(ClassLoader.java:248)</p>
<p>Any suggestions as to how to get it running? I am using java version "1.6.0_22"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '11, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/2f27809e645aec011de4d9ac938c53f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="George&#39;s gravatar image" />
<p><span>George</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="George has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3214" class="comments-container">
&#10;</div>
<div id="comment-tools-3214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3214-form-container" class="comment-form-container">
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

<span id="3237"></span>

<div id="answer-container-3237" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3237-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="George has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'ure using the java command in a wrong way. The bin/osmosis file is a shell script, not a java class file, so you have to run it like that: /Users/George/Downloads/osmosis-0.38/bin/osmosis If the file isn't executable, run that before: chmod +x /Users/George/Downloads/osmosis-0.38/bin/osmosis</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '11, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-3237" class="comments-container">
<span id="3243"></span>
<div id="comment-3243" class="comment">
<div id="post-3243-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, works perfectly!</p>
</div>
<div id="comment-3243-info" class="comment-info">
<span class="comment-age">(21 Feb '11, 21:17)</span> <span class="comment-user userinfo">George</span>
</div>
</div>
</div>
<div id="comment-tools-3237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3237-form-container" class="comment-form-container">
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


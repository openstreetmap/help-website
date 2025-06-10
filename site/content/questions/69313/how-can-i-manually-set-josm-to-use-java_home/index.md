+++
type = "question"
title = "How can I manually set JOSM to use JAVA_HOME"
description = '''I am using High Sierra OSX 10.13.6 and recently installed Java 12. However, JOSM (I am running the most recent version) insists on loading Java 8. I have properly set JAVA_HOME and if I run JOSM from a terminal session, it invokes JAVA 12 like it should. This is clearly some &quot;FEATURE&quot; that Apple has...'''
date = "2019-05-26T05:53:00Z"
lastmod = "2019-05-27T04:12:00Z"
weight = 69313
keywords = [ "josm", "java", "preferences" ]
aliases = [ "/questions/69313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I manually set JOSM to use JAVA_HOME](/questions/69313/how-can-i-manually-set-josm-to-use-java_home)

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
<span id="post-69313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69313-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using High Sierra OSX 10.13.6 and recently installed Java 12. However, JOSM (I am running the most recent version) insists on loading Java 8. I have properly set JAVA_HOME and if I run JOSM from a terminal session, it invokes JAVA 12 like it should. This is clearly some "FEATURE" that Apple has made available (the Java Console shoes that Java 8 is still reflected as the current plugin, because Java 12 does not have a java plugin. I even renamed the Home directory in the plugin directory and linked the java 12 Home to it, and I got a JOSM loading error.</p>
<p>How do I configure whatever prefs file plist file that controls JOSM to use Java 12? I looked in both I cold find, and there seems to be nothing there, though JOSM says that the selection of Java 8 is in the preferences file....</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '19, 05:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e4cadcf9f86d306510a1e19319359877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net-buoy&#39;s gravatar image" />
<p><span>net-buoy</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net-buoy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69313" class="comments-container">
&#10;</div>
<div id="comment-tools-69313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69313-form-container" class="comment-form-container">
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

<span id="69314"></span>

<div id="answer-container-69314" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69314-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you trying to use the jnlp of JOSM? I thought that Oracle removed that feature from Java, so it is no longer possible to use webstart with Java 12. If you really want to use Java 12 to run Josm, you have to download the jar version and start that your Java 12 from the command line.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '19, 06:24</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-69314" class="comments-container">
<span id="69316"></span>
<div id="comment-69316" class="comment">
<div id="post-69316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded <a href="https://josm.openstreetmap.de/download/macosx/josm-macosx.zip">https://josm.openstreetmap.de/download/macosx/josm-macosx.zip</a> which is an JOSM.app that can be placed in Applications with the current jar (josm-snapshot-15031.jar) which is the same as latest-tested.jar. So, no I am NOT running jnlp, I am running the jar. There is some setting somewhere in OSX that is telling the app to use the plugin as even when I change the name of the jdk, JOSM still runs using the plugin from Java 8 :-(</p>
<p>SO, JOSM does run as an app from the jar, but it is sourcing the internet java plugin, instead of the installed JDK, and Java 12 won't overwrite the plugin because it does not come with one. Now, if I remove the jaba plugin, I am afraid that JOSM won;t run at all, hence I want to figure out how JOSM is sourcing a java version on J=High Sierra, and just change the source.</p>
</div>
<div id="comment-69316-info" class="comment-info">
<span class="comment-age">(26 May '19, 06:38)</span> <span class="comment-user userinfo">net-buoy</span>
</div>
</div>
<span id="69328"></span>
<div id="comment-69328" class="comment">
<div id="post-69328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On one of the machines on which I run JOSM, I have removed the Java plugin without problems, but I'm still using Java 8 form AdoptOpenJDK on that machine. I wonder which runtime libraries are missing from Java 12 (see <a href="https://weeklyosm.eu/josm-and-java-and-the-german-forum">https://weeklyosm.eu/josm-and-java-and-the-german-forum</a> for ta full list of problems caused by Oracle's new Java Policy)</p>
</div>
<div id="comment-69328-info" class="comment-info">
<span class="comment-age">(27 May '19, 04:12)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-69314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69314-form-container" class="comment-form-container">
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


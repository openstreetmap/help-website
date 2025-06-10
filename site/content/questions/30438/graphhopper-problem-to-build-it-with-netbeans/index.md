+++
type = "question"
title = "Graphhopper problem to build it with Netbeans"
description = '''I download graphhopper and I open the &quot;Graphhopper Web&quot; project in Netbeans, I build It(and the result is BUILD SUCCES) but It doesn&#x27;t open a web page with the result and there are to many errors(in Graphhopper web) as: The module has not been deployed. See the server log for details.  at org.netbea...'''
date = "2014-02-04T10:41:00Z"
lastmod = "2014-02-07T14:20:00Z"
weight = 30438
keywords = [ "graphhopper" ]
aliases = [ "/questions/30438" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Graphhopper problem to build it with Netbeans](/questions/30438/graphhopper-problem-to-build-it-with-netbeans)

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
<span id="post-30438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I download graphhopper and I open the "Graphhopper Web" project in Netbeans, I build It(and the result is BUILD SUCCES) but It doesn't open a web page with the result and there are to many errors(in Graphhopper web) as:</p>
<pre><code>The module has not been deployed.
See the server log for details.
    at org.netbeans.modules.j2ee.deployment.devmodules.api.Deployment.deploy(Deployment.java:238)
    at org.netbeans.modules.maven.j2ee.ExecutionChecker.performDeploy(ExecutionChecker.java:205)
    at org.netbeans.modules.maven.j2ee.ExecutionChecker.executionResult(ExecutionChecker.java:123)
    at org.netbeans.modules.maven.execute.MavenCommandLineExecutor.run(MavenCommandLineExecutor.java:235)
    at org.netbeans.core.execution.RunClassThread.run(RunClassThread.java:153)</code></pre>
<p>And there are so many errors in "Glassfish server 4.0":</p>
<pre><code>Grave:   Startup of context /web failed due to previous errors
Grave:   Exception during cleanup after start failed
Grave:   ContainerBase.addChild: start: 
Avvertenza:   java.lang.IllegalStateException: ContainerBase.addChild: start: org.apache.catalina.LifecycleException: com.google.inject.CreationException: Guice creation errors:
Grave:   Exception during lifecycle processing
Grave:   Exception while loading the app
Grave:   Undeployment failed for context /web
Grave:   Exception while loading the app : java.lang.IllegalStateException: ContainerBase.addChild: start: org.apache.catalina.LifecycleException: com.google.inject.CreationException: Guice creation errors:</code></pre>
<p>and other....</p>
<p>I don't understand how to build this project and why there is all these errors, can you help me? Thank you.</p>
<p>EDIT: I edit because i solved the first question, and i open a web pages: localhost:8989 where there is the berlin map</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '14, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/3be508f311801a447f51a4dab36a0e57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoifil&#39;s gravatar image" />
<p><span>Zoifil</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoifil has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '14, 10:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-30438" class="comments-container">
<span id="30534"></span>
<div id="comment-30534" class="comment">
<div id="post-30534-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>nobody can help me? I think that the problem is that the map wasn't find</p>
</div>
<div id="comment-30534-info" class="comment-info">
<span class="comment-age">(07 Feb '14, 13:28)</span> <span class="comment-user userinfo">Zoifil</span>
</div>
</div>
<span id="30535"></span>
<div id="comment-30535" class="comment">
<div id="post-30535-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>AFAIK Graphhopper has a very limited community even within OSM, so I guess it's more useful to ask this very specific question at the GH support chanels <a href="http://graphhopper.com/#contact">http://graphhopper.com/#contact</a></p>
</div>
<div id="comment-30535-info" class="comment-info">
<span class="comment-age">(07 Feb '14, 13:32)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="30537"></span>
<div id="comment-30537" class="comment">
<div id="post-30537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the reply but I have already ask on the link you have write..</p>
</div>
<div id="comment-30537-info" class="comment-info">
<span class="comment-age">(07 Feb '14, 14:20)</span> <span class="comment-user userinfo">Zoifil</span>
</div>
</div>
</div>
<div id="comment-tools-30438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30438-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


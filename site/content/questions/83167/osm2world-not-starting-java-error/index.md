+++
type = "question"
title = "OSM2WORLD not starting - java error"
description = '''I&#x27;ve exported a world to osm from OpenStreetMap, and I wanted to open it in osm2world, but it won&#x27;t open. I have java 17.01 installed and every time I start the program in CMD, it throws up this message: C:&#92;Users&#92;User&#92;Downloads&#92;OSM2World-latest-bin&amp;gt;java -Xmx2G -jar OSM2World.jar No parameters, ru...'''
date = "2022-01-23T18:19:00Z"
lastmod = "2022-01-23T20:15:00Z"
weight = 83167
keywords = [ "osm2world", "windows", "java", "opengl" ]
aliases = [ "/questions/83167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM2WORLD not starting - java error](/questions/83167/osm2world-not-starting-java-error)

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
<span id="post-83167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83167-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've exported a world to osm from OpenStreetMap, and I wanted to open it in osm2world, but it won't open. I have java 17.01 installed and every time I start the program in CMD, it throws up this message:</p>
<p><em>C:\Users\User\Downloads\OSM2World-latest-bin&gt;java -Xmx2G -jar OSM2World.jar No parameters, running graphical interface. If you want to use the command line, use the --help parameter for a list of available parameters. No --config parameter, using default style (standard.properties). FPSAnimator P1:Thread[main-FPSAWTAnimator-Timer0,5,main]: Task[thread Thread[main-FPSAWTAnimator-Timer0,5,main], stopped false, paused false shouldRun true, shouldStop false -- started true, animating true, paused false, drawable 1, drawablesEmpty false] Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 1 at jogamp.opengl.windows.wgl.awt.WindowsAWTWGLGraphicsConfigurationFactory.chooseGraphicsConfigurationImpl(WindowsAWTWGLGraphicsConfigurationFactory.java:169) at javax.media.nativewindow.GraphicsConfigurationFactory.chooseGraphicsConfiguration(GraphicsConfigurationFactory.java:420) at javax.media.opengl.awt.GLCanvas.chooseGraphicsConfiguration(GLCanvas.java:1186) at javax.media.opengl.awt.GLCanvas.addNotify(GLCanvas.java:572) at java.desktop/java.awt.Container.addNotify(Container.java:2804) at java.desktop/javax.swing.JComponent.addNotify(JComponent.java:4839) at java.desktop/java.awt.Container.addNotify(Container.java:2804) at java.desktop/javax.swing.JComponent.addNotify(JComponent.java:4839) at java.desktop/java.awt.Container.addNotify(Container.java:2804) at java.desktop/javax.swing.JComponent.addNotify(JComponent.java:4839) at java.desktop/javax.swing.JRootPane.addNotify(JRootPane.java:729) at java.desktop/java.awt.Container.addNotify(Container.java:2804) at java.desktop/java.awt.Window.addNotify(Window.java:791) at java.desktop/java.awt.Frame.addNotify(Frame.java:495) at java.desktop/java.awt.Window.pack(Window.java:829) at org.osm2world.viewer.view.ViewerFrame.&lt;init&gt;(ViewerFrame.java:123) at org.osm2world.console.OSM2World.executeArgumentsGroup(OSM2World.java:210)</em></p>
<p>My only guess is that Java isn't starting a graphics library or something. Could it be that I don't have a newer version of java installed? Any help would be greatly appreciated. (P.S. I used the batch file to start it, and also tried the .jar file)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2world" rel="tag" title="see questions tagged &#39;osm2world&#39;">osm2world</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-opengl" rel="tag" title="see questions tagged &#39;opengl&#39;">opengl</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '22, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/bed7243ed021abaef211ec0a340c3b29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Youdubham&#39;s gravatar image" />
<p><span>Youdubham</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Youdubham has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83167" class="comments-container">
&#10;</div>
<div id="comment-tools-83167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83167-form-container" class="comment-form-container">
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

<span id="83170"></span>

<div id="answer-container-83170" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83170-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error is caused by the JOGL library that OSM2World relies on for OpenGL rendering.</p>
<p>At the time of writing, that library still requires Java 8 (<strong>not</strong> "Java 8 or newer"), so your first step to get it to work would be to install this older version of Java.</p>
<p>Alternatively, you might be able to avoid the use of OpenGL (and therefore the graphical interface of OSM2World) by running a conversion entirely from the command line with suitable input &amp; output parameters. But that depends on what you want to achieve.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '22, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-83170" class="comments-container">
&#10;</div>
<div id="comment-tools-83170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83170-form-container" class="comment-form-container">
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


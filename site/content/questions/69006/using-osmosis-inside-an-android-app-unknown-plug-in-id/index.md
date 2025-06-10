+++
type = "question"
title = "Using osmosis inside an Android app - unknown plug-in ID"
description = '''Hello, I want to convert a .osm file (previously downloaded) to a .map file using Osmosis and Mapforge&#x27;s mapfile-writer inside an Android application. To do so, I created a new project (I am using Android Studio) I imported the osmosis-core library (using implementation &#x27;org.openstreetmap.osmosis:os...'''
date = "2019-04-29T14:44:00Z"
lastmod = "2019-04-30T07:23:00Z"
weight = 69006
keywords = [ "osmosis", "android", "exception", "library", "plugin" ]
aliases = [ "/questions/69006" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using osmosis inside an Android app - unknown plug-in ID](/questions/69006/using-osmosis-inside-an-android-app-unknown-plug-in-id)

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
<span id="post-69006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69006-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to convert a .osm file (previously downloaded) to a .map file using Osmosis and Mapforge's mapfile-writer inside an Android application.</p>
<p>To do so, I created a new project (I am using Android Studio)</p>
<p>I imported the osmosis-core library (using <code>implementation 'org.openstreetmap.osmosis:osmosis-core:0.43-RELEASE'</code> in the build.gradle file)</p>
<p>I created a class with a public void main which calls <code>Osmosis.run(new String[]{"--read-xml mapUPS.osm --mapfile-writer file=mapUPS.map"});</code></p>
<p>But i am getting this error :</p>
<p><code>java.lang.IllegalArgumentException: unknown plug-in ID - org.openstreetmap.osmosis.core.plugin.Core at org.java.plugin.registry.xml.PluginRegistryImpl.getPluginDescriptor(PluginRegistryImpl.java:729) at org.openstreetmap.osmosis.core.TaskRegistrar.registerCorePlugin(TaskRegistrar.java:212) at org.openstreetmap.osmosis.core.TaskRegistrar.loadJPFPlugins(TaskRegistrar.java:159) at org.openstreetmap.osmosis.core.TaskRegistrar.initialize(TaskRegistrar.java:88) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:81)</code></p>
<p>I don't know where is the problem. Where am I wrong ?</p>
<p>Thank you in advance,</p>
<p>iomega11</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '19, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/81c5ab54e7cef12bce26ca979fd4fd19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iomega111&#39;s gravatar image" />
<p><span>iomega111</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iomega111 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '19, 09:39</strong> </span></p>
</div>
</div>
<div id="comments-container-69006" class="comments-container">
&#10;</div>
<div id="comment-tools-69006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69006-form-container" class="comment-form-container">
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

<span id="69007"></span>

<div id="answer-container-69007" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69007-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I understand what you are doing correctly you are essentially trying to run the command line version of osmosis on Android, I'm not ruling out that you could get it to work, but the Android JVM differs in a number of ways from "standard" Java and I'm actually slightly surprised you got as far as you did.</p>
<p>Using the various bits and pieces of osmosis as a library should however work, you just need to write the corresponding glue that joins everything together. For example I use the Osmosis's PBF reading support in <a href="http://vespiccu.io/">Vespucci</a>. If you are doing format conversion you will likely be rather limited in the size of OSM extracts you can convert.</p>
<p>Maybe you should explain a bit more what you actually want to achieve.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '19, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69007" class="comments-container">
<span id="69014"></span>
<div id="comment-69014" class="comment">
<div id="post-69014-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SimonPoole, thanks for your reply.</p>
<p>On my computer I use osmosis via this command :</p>
<p>osmosis --read-xml mapUPS.osm --mapfile-writer file=mapUPS.map</p>
<p>I want to convert a .osm file (previously downloaded) to a .map file using Osmosis and Mapforge's mapfile-writer.</p>
<p>I have never heard of the Vespucci app, I will look at how osmosis is used in this app, in order to do the same with my app.</p>
<p>Thanks a lot !</p>
<p>iomega111</p>
</div>
<div id="comment-69014-info" class="comment-info">
<span class="comment-age">(30 Apr '19, 07:23)</span> <span class="comment-user userinfo">iomega111</span>
</div>
</div>
</div>
<div id="comment-tools-69007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69007-form-container" class="comment-form-container">
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


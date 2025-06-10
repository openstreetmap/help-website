+++
type = "question"
title = "Not a GraphHopper file! Expected &#x27;GH&#x27; as file marker but was"
description = '''Hi everyone. Last night i`ve got latest &quot;planet-latest.osm.pbf&quot; and tried to compile files for railroads but got next error: java -d64 -Xmx16g -XX:+UseG1GC -server -jar graphhopper-web-0.3-with-rail.jar jetty.port=9999 jetty.resourcebase=webapp config=rail.properties osmreader.osm=planet-latest.osm....'''
date = "2015-07-13T17:49:00Z"
lastmod = "2015-07-14T16:51:00Z"
weight = 44164
keywords = [ "not", "a", "graphhopper", "file" ]
aliases = [ "/questions/44164" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not a GraphHopper file! Expected 'GH' as file marker but was](/questions/44164/not-a-graphhopper-file-expected-gh-as-file-marker-but-was)

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
<span id="post-44164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44164-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone.</p>
<p>Last night i`ve got latest "<strong>planet-latest.osm.pbf</strong>" and tried to compile files for railroads but got next error:</p>
<pre><code>java -d64 -Xmx16g -XX:+UseG1GC -server -jar graphhopper-web-0.3-with-rail.jar jetty.port=9999 jetty.resourcebase=webapp config=rail.properties osmreader.osm=planet-latest.osm.pbf</code></pre>
<p>I<code>ve tried to do the same at friday and it works well, but now i got the message. Also i</code>ve tried to restart "<strong>osmupdate</strong>" but this doesn`t help. Any ideas why i got this message? Thanks in advance guys.</p>
<pre><code>Jul 13, 2015 4:33:27 PM com.google.inject.internal.MessageProcessor visit
&#10;**INFO: An exception was caught and reported. Message: java.lang.IllegalArgumentException: Not a GraphHopper file! Expected &#39;GH&#39; as file marker but was**
&#10;java.lang.IllegalStateException: Couldn&#39;t load graph
        at com.graphhopper.http.DefaultModule.configure(DefaultModule.java:60)
        at com.google.inject.AbstractModule.configure(AbstractModule.java:59)
        at com.google.inject.spi.Elements$RecordingBinder.install(Elements.java:223)
        at com.google.inject.AbstractModule.install(AbstractModule.java:118)
        at com.graphhopper.http.GHServer$1.configure(GHServer.java:111)
        at com.google.inject.AbstractModule.configure(AbstractModule.java:59)
        at com.google.inject.spi.Elements$RecordingBinder.install(Elements.java:223)
        at com.google.inject.spi.Elements.getElements(Elements.java:101)
        at com.google.inject.internal.InjectorShell$Builder.build(InjectorShell.java:133)
        at com.google.inject.internal.InternalInjectorCreator.build(InternalInjectorCreator.java:103)
        at com.google.inject.Guice.createInjector(Guice.java:95)
        at com.google.inject.Guice.createInjector(Guice.java:72)
        at com.google.inject.Guice.createInjector(Guice.java:62)
        at com.graphhopper.http.GHServer.start(GHServer.java:61)
        at com.graphhopper.http.GHServer.main(GHServer.java:47)
&#10;Caused by: java.lang.IllegalArgumentException: Not a GraphHopper file! Expected &#39;GH&#39; as file marker but was 
        at com.graphhopper.storage.AbstractDataAccess.readHeader(AbstractDataAccess.java:118)
        at com.graphhopper.storage.MMapDataAccess.loadExisting(MMapDataAccess.java:236)
        at com.graphhopper.storage.SynchedDAWrapper.loadExisting(SynchedDAWrapper.java:141)
        at com.graphhopper.storage.GraphHopperStorage.loadExisting(GraphHopperStorage.java:1355)
        at com.graphhopper.GraphHopper.load(GraphHopper.java:679)
        at com.graphhopper.GraphHopper.importOrLoad(GraphHopper.java:557)
        at com.graphhopper.http.DefaultModule.configure(DefaultModule.java:47)
        ... 14 more
&#10;**Exception in thread &quot;main&quot; com.google.inject.CreationException: Guice creation errors:**
&#10;1) An exception was caught and reported. Message: Couldn&#39;t load graph
  at com.graphhopper.http.GHServer$1.configure(GHServer.java:111)
&#10;2) Explicit bindings are required and com.graphhopper.GraphHopper is not explicitly bound.
  while locating com.graphhopper.GraphHopper
    for field at com.graphhopper.http.GraphHopperServlet.hopper(GraphHopperServlet.java:45)
  at com.graphhopper.http.GHServletModule.configureServlets(GHServletModule.java:60)
&#10;3) Explicit bindings are required and com.graphhopper.util.TranslationMap is not explicitly bound.
  while locating com.graphhopper.util.TranslationMap
    for field at com.graphhopper.http.I18NServlet.map(I18NServlet.java:35)
  at com.graphhopper.http.GHServletModule.configureServlets(GHServletModule.java:54)
&#10;4) Explicit bindings are required and com.graphhopper.GraphHopper is not explicitly bound.
  while locating com.graphhopper.GraphHopper
    for field at com.graphhopper.http.InfoServlet.hopper(InfoServlet.java:39)
  at com.graphhopper.http.GHServletModule.configureServlets(GHServletModule.java:57)
&#10;**4 errors**
        at com.google.inject.internal.Errors.throwCreationExceptionIfErrorsExist(Errors.java:435)
        at com.google.inject.internal.InternalInjectorCreator.initializeStatically(InternalInjectorCreator.java:154)
        at com.google.inject.internal.InternalInjectorCreator.build(InternalInjectorCreator.java:106)
        at com.google.inject.Guice.createInjector(Guice.java:95)
        at com.google.inject.Guice.createInjector(Guice.java:72)
        at com.google.inject.Guice.createInjector(Guice.java:62)
        at com.graphhopper.http.GHServer.start(GHServer.java:61)
        at com.graphhopper.http.GHServer.main(GHServer.java:47)
Caused by: java.lang.IllegalStateException: Couldn&#39;t load graph
        at com.graphhopper.http.DefaultModule.configure(DefaultModule.java:60)
        at com.google.inject.AbstractModule.configure(AbstractModule.java:59)
        at com.google.inject.spi.Elements$RecordingBinder.install(Elements.java:223)
        at com.google.inject.AbstractModule.install(AbstractModule.java:118)
        at com.graphhopper.http.GHServer$1.configure(GHServer.java:111)
        at com.google.inject.AbstractModule.configure(AbstractModule.java:59)
        at com.google.inject.spi.Elements$RecordingBinder.install(Elements.java:223)
        at com.google.inject.spi.Elements.getElements(Elements.java:101)
        at com.google.inject.internal.InjectorShell$Builder.build(InjectorShell.java:133)
        at com.google.inject.internal.InternalInjectorCreator.build(InternalInjectorCreator.java:103)
        ... 5 more
Caused by: java.lang.IllegalArgumentException: Not a GraphHopper file! Expected &#39;GH&#39; as file marker but was 
        at com.graphhopper.storage.AbstractDataAccess.readHeader(AbstractDataAccess.java:118)
        at com.graphhopper.storage.MMapDataAccess.loadExisting(MMapDataAccess.java:236)
        at com.graphhopper.storage.SynchedDAWrapper.loadExisting(SynchedDAWrapper.java:141)
        at com.graphhopper.storage.GraphHopperStorage.loadExisting(GraphHopperStorage.java:1355)
        at com.graphhopper.GraphHopper.load(GraphHopper.java:679)
        at com.graphhopper.GraphHopper.importOrLoad(GraphHopper.java:557)
        at com.graphhopper.http.DefaultModule.configure(DefaultModule.java:47)
        **... 14 more**
&#10;
**ubuntu@ip-172:/gh/generator$ java -version**
java version &quot;1.7.0_65&quot;
OpenJDK Runtime Environment (IcedTea 2.5.3) (7u71-2.5.3-0ubuntu0.14.04.1)
OpenJDK 64-Bit Server VM (build 24.65-b04, mixed mode)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-a" rel="tag" title="see questions tagged &#39;a&#39;">a</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '15, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9ab74ed3a5230aa97fd7e06510caba64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey%20Logicov&#39;s gravatar image" />
<p><span>Andrey Logicov</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey Logicov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '15, 16:35</strong> </span></p>
</div>
</div>
<div id="comments-container-44164" class="comments-container">
<span id="44167"></span>
<div id="comment-44167" class="comment">
<div id="post-44167-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In case you do not get an answer here, you could try the <a href="https://lists.openstreetmap.org/listinfo/graphhopper">graphhopper mailing list</a></p>
</div>
<div id="comment-44167-info" class="comment-info">
<span class="comment-age">(13 Jul '15, 19:48)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-44164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44164-form-container" class="comment-form-container">
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

<span id="44181"></span>

<div id="answer-container-44181" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44181-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, I cannot comment here so I have to answer although I have no answer ... just some hints:</p>
<ul>
<li>If you want to do a reimport e.g. when your pbf updated you have to completely remove the graphhopper folder</li>
<li>Did you try with a smaller area and does this work?</li>
<li>Are you using normal HDD or SSD or some virtual filesystem?</li>
<li>Did the last import properly run through?</li>
<li>How much RAM do you have on your machine? If you are using some MMAP config make sure you leave enough RAM for the OS and do not assign all to the JVM</li>
<li>It is recommended to use the latest version 0.4 instead of 0.3, there were many bug fixes already</li>
</ul>
<p>PS: You should proper format the stacktrace, this is a bit irritating :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '15, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-44181" class="comments-container">
&#10;</div>
<div id="comment-tools-44181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44181-form-container" class="comment-form-container">
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


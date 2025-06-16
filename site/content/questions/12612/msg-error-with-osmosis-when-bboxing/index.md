+++
type = "question"
title = "Msg error with osmosis when bboxing"
description = '''Hi, I would like to make an extract with Osmosis for the Bahia state in Brazil from the brasil.osm.bz2 file that can be found on http://download.geofabrik.de/osm/south-america/  osmosis --read-xml file=&quot;D:/OSM/Salvador/brazil.osm&quot; --bounding-polygon file=&quot;D:/OSM/Salvador/Bahia_contour.poly&quot; --write-...'''
date = "2012-05-08T16:23:00Z"
lastmod = "2012-05-08T16:23:00Z"
weight = 12612
keywords = [ "bounding-polygon", "osmosis" ]
aliases = [ "/questions/12612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Msg error with osmosis when bboxing](/questions/12612/msg-error-with-osmosis-when-bboxing)

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
<span id="post-12612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12612-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would like to make an extract with Osmosis for the Bahia state in Brazil from the brasil.osm.bz2 file that can be found on <a href="http://download.geofabrik.de/osm/south-america/">http://download.geofabrik.de/osm/south-america/</a></p>
<blockquote>
<p>osmosis --read-xml file="D:/OSM/Salvador/brazil.osm" --bounding-polygon file="D:/OSM/Salvador/Bahia_contour.poly" --write-xml file="D:/OSM/Salvador/bahia.osm"</p>
</blockquote>
<p>My specs are :</p>
<ul>
<li>OS Vista SP1</li>
<li>Osmosis 0.40.1 (installed by running a frist osmosis as indicated here <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Installation">https://wiki.openstreetmap.org/wiki/Osmosis/Installation</a> )</li>
</ul>
<p>I get this error message :</p>
<pre><code>D:\OSM\osmosis-0.40.1\bin&gt;osmosis --read-xml
file=&quot;D:/OSM/Salvador/brazil.osm&quot; -
-bounding-polygon file=&quot;D:/OSM/Salvador/Bahia_contour.poly&quot; --write-xml
file=&quot;D:
/OSM/Salvador/bahia.osm&quot;
6 mai 2012 11:28:36 org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
6 mai 2012 11:28:36 org.java.plugin.registry.xml.ManifestParser &lt;init&gt;
INFO: got SAX parser factory -
org.apache.xerces.jaxp.SAXParserFactoryImpl at 45a87
7
6 mai 2012 11:28:36 org.java.plugin.registry.xml.PluginRegistryImpl
configure
INFO: configured, stopOnError=false, isValidating=true
6 mai 2012 11:28:37 org.java.plugin.registry.xml.PluginRegistryImpl register
INFO: plug-in and fragment descriptors registered - 1
6 mai 2012 11:28:37 org.java.plugin.standard.StandardPluginManager
activatePlugi
n
INFO: plug-in started - org.openstreetmap.osmosis.core.plugin.Core at 0.40.1
6 mai 2012 11:28:37 org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
6 mai 2012 11:28:37 org.openstreetmap.osmosis.core.Osmosis main
GRAVE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: The following named
pipe
s () and 1 default pipes have not been terminated with appropriate output
sinks.
&#10;        at
org.openstreetmap.osmosis.core.pipeline.common.Pipeline.connectTasks(
Pipeline.java:94)
        at
org.openstreetmap.osmosis.core.pipeline.common.Pipeline.prepare(Pipel
 ine.java:116)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:86)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at
org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun
cher.java:329)
        at
org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav
a:239)
        at
org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La
uncher.java:409)
        at
org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:
352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>Does anyone have an idea where is my mistake ?</p>
<p>Sincerely,</p>
<p>Severin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '12, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/35a2e88e2106806c0ba99b9b5e6ef093?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeverinGeo&#39;s gravatar image" />
<p><span>SeverinGeo</span><br />
<span class="score" title="81 reputation points">81</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeverinGeo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '12, 16:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-12612" class="comments-container">
&#10;</div>
<div id="comment-tools-12612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12612-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


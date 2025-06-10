+++
type = "question"
title = "Osmosis creating huge files with many tags when"
description = '''Hi I have several troubles when running Osmosis: 1 - when I run  osmosis --read-xml file=&quot;map1.osm&quot; --bounding-box top=47.3532684 left=-1.9217581 bottom=47.1023462 right=-1.3584780 --way-key-value keyValueList=&quot;railway.tram&quot;  --write-xml file=&quot;map2-tram.osm&quot; Osmosis will make a huge file of more tha...'''
date = "2012-03-26T15:10:00Z"
lastmod = "2012-03-26T15:10:00Z"
weight = 11506
keywords = [ "osmosis" ]
aliases = [ "/questions/11506" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis creating huge files with many tags when](/questions/11506/osmosis-creating-huge-files-with-many-tags-when)

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
<span id="post-11506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11506-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I have several troubles when running Osmosis:</p>
<p>1 - when I run osmosis --read-xml file="map1.osm" --bounding-box top=47.3532684 left=-1.9217581 bottom=47.1023462 right=-1.3584780 --way-key-value keyValueList="railway.tram"  --write-xml file="map2-tram.osm"</p>
<p>Osmosis will make a huge file of more than 300 Mb with any ways and nodes instead of only trams. If i add the --used-node option, i will get a rather smaller file of 27 Gb but with ton of useless nodes likes bus stops or elevation points, speed cameras, street numbers...... While I only want tram routes and stops... There are only 3 to be imported, so I should get a small 3 mb file.</p>
<p>I have same problem with highways.</p>
<p>2 - If I run the command osmosis --read-xml file="map1.osm" --bounding-box top=47.3532684 left=-1.9217581 bottom=47.1023462 right=-1.3584780 --tf accept-ways railway=tram,tram_stop --tf reject-ways railway=* --used-node --write-xml file="map2-highways.osm" I will not get better job. It will import me everything instead of tramway routes only...</p>
<p>3 - If I do it in 2 steps, first extracting the bounding box, then the tags I will get the following error "org.openstreetmap.osmosis.core.OsmosisRuntimeException: Task type way-key-value?keyValueList=railway.tram,railway.tram_stop, railway.rail doesn't exist." ! They do exist I made a fast import in QGIS and saw there were railways in the file itself....</p>
<p>4 - If I do the same but with nodes only this time, i dn't know, like restaurants for example, it works perfectly. osmosis --read-xml file="map1.osm" --bounding-box top=47.3532684 left=-1.9217581 bottom=47.1023462 right=-1.3584780 --node-key-value keyValueList="amenity.restaurant,amenity.fast_food" --write-xml file="map2-restaurant.osm"</p>
<p>Mac OS X 10.6.8 / Osmosis 0.40.1</p>
<blockquote>
<p>org.openstreetmap.osmosis.core.OsmosisRuntimeException: Task type version doesn't exist. at org.openstreetmap.osmosis.core.pipeline.common.TaskManagerFactoryRegister.getInstance(TaskManagerFactoryRegister.java:60) at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.buildTasks(Pipeline.java:50) at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.prepare(Pipeline.java:112) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:86) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25) at java.lang.reflect.Method.invoke(Method.java:597) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352) at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '12, 15:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0386112b51bf4ff150fab7b2d180ce1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rick75&#39;s gravatar image" />
<p><span>Rick75</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rick75 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Mar '12, 20:19</strong> </span></p>
</div>
</div>
<div id="comments-container-11506" class="comments-container">
&#10;</div>
<div id="comment-tools-11506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11506-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


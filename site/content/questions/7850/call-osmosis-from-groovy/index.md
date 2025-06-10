+++
type = "question"
title = "[closed] call osmosis from groovy"
description = '''Hi, i have to merge a lot of small *.osm files together.  The first try was to create a windows .bat file but the command line was longer than supported from windows. Now i wrote 2 groovy scripts and call osmosis directly. Unfortunately it looks like it can&#x27;t find/load plugins:  org.openstreetmap.os...'''
date = "2011-09-14T11:31:00Z"
lastmod = "2011-09-15T17:25:00Z"
weight = 7850
keywords = [ "groovy", "osmosis" ]
aliases = [ "/questions/7850" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] call osmosis from groovy](/questions/7850/call-osmosis-from-groovy)

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
<span id="post-7850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7850-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-7850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>i have to merge a lot of small *.osm files together.</p>
<p>The first try was to create a windows .bat file but the command line was longer than supported from windows.</p>
<p>Now i wrote 2 groovy scripts and call osmosis directly. Unfortunately it looks like it can't find/load plugins: <code>org.openstreetmap.osmosis.core.OsmosisRuntimeException: Task type fast-read-xml</code></p>
<p>There are the groovy files: merge.groovy <code> String localDirectory = new File(getClass().protectionDomain.codeSource.location.path).parent String urlBase = "file:/" + localDirectory + "osmosis-0.39\lib\default\"; URL[] urls = [new URL(urlBase + "plexus-classworlds-2.2.2.jar")]; ClassLoader classLoader = new URLClassLoader(urls, getClass().getClassLoader()); GroovyShell myGroovyShell4Merge = new GroovyShell(classLoader, binding); processErrorStatus = myGroovyShell4Merge.evaluate(new File(localDirectory, "/innerMergeCall.groovy")) </code></p>
<p>innerMergeCall.groovy <code> String localDirectory = new File(getClass().protectionDomain.codeSource.location.path).parent File dir = new File("tmp/osm_parts"); if(dir.isDirectory()) { List argsList = new ArrayList() String[] subFiles = dir.list() long count = 0; for(String fileStr : subFiles) { argsList.add("--fast-read-xml " + new File(dir, fileStr).canonicalPath) count++ } for(int ii = 1; ii &lt; count; ii++) { argsList.add("--merge") } argsList.add("--wx " + new File(localDirectory, "tmp/osm/merged.osm")) String[] args = new String[argsList.size()] args = argsList.toArray(args) String myAppHome = new File(localDirectory, "osmosis-0.39").canonicalPath System.setProperty("app.home", myAppHome) System.setProperty("classworlds.conf", myAppHome + "/config/plexus.conf") org.codehaus.classworlds.Launcher.main(args) } </code></p>
<p>Does anyone have an idea what going wrong?</p>
<p>Yours Rüdiger</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-groovy" rel="tag" title="see questions tagged &#39;groovy&#39;">groovy</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '11, 11:31</strong></p>
<img src="https://secure.gravatar.com/avatar/75e5e762d630a85a2deec2421fa28f98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgubler&#39;s gravatar image" />
<p><span>rgubler</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgubler has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>14 Sep '11, 16:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-7850" class="comments-container">
<span id="7857"></span>
<div id="comment-7857" class="comment">
<div id="post-7857-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This help website is not relevant for such software issues. Please contact the dev@<a href="http://openstreetmap.org">openstreetmap.org</a> or osmosis-dev@<a href="http://openstreetmap.org">openstreetmap.org</a> mailing lists where you might have a better chance to get an answer.</p>
</div>
<div id="comment-7857-info" class="comment-info">
<span class="comment-age">(14 Sep '11, 16:52)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="7899"></span>
<div id="comment-7899" class="comment">
<div id="post-7899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... or ask at <a href="http://forum.osm.org">http://forum.osm.org</a></p>
</div>
<div id="comment-7899-info" class="comment-info">
<span class="comment-age">(15 Sep '11, 17:25)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-7850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7850-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Pieren 14 Sep '11, 16:49

</div>

</div>

</div>


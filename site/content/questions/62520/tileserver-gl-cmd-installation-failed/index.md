+++
type = "question"
title = "tileserver-gl cmd installation failed"
description = '''Trying to setup vector tiles server with static image support. Referring http://tileserver.readthedocs.io/en/latest/installation.html and https://github.com/klokantech/tileserver-gl While trying to install tileserver-gl command in my mac machine and in a centos machine, met below err. (alignment is ...'''
date = "2018-03-06T08:07:00Z"
lastmod = "2018-03-08T10:47:00Z"
weight = 62520
keywords = [ "staticmap", "tileserver", "vector", "mapbox" ]
aliases = [ "/questions/62520" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tileserver-gl cmd installation failed](/questions/62520/tileserver-gl-cmd-installation-failed)

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
<span id="post-62520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Trying to setup vector tiles server with static image support. Referring <a href="http://tileserver.readthedocs.io/en/latest/installation.html">http://tileserver.readthedocs.io/en/latest/installation.html</a> and <a href="https://github.com/klokantech/tileserver-gl">https://github.com/klokantech/tileserver-gl</a></p>
<p>While trying to install tileserver-gl command in my mac machine and in a centos machine, met below err. (alignment is not easy here ?)</p>
<pre><code>npm WARN deprecated nomnom@1.8.1: Package no longer supported. Contact support@npmjs.com for more info.
npm WARN lifecycle @mapbox/mapbox-gl-native@3.5.4~preinstall: cannot run in wd %s %s (wd=%s) @mapbox/mapbox-gl-native@3.5.4 npm install node-pre-gyp /usr/local/lib/node_modules/.staging/@mapbox/mapbox-gl-native-74bf2b00
/usr/local/bin/tileserver-gl -&gt; /usr/local/lib/node_modules/tileserver-gl/src/main.js
&#10;&gt; sqlite3@3.1.13 install /usr/local/lib/node_modules/tileserver-gl/node_modules/sqlite3
&gt; node-pre-gyp install --fallback-to-build
&#10;[sqlite3] Success: &quot;/usr/local/lib/node_modules/tileserver-gl/node_modules/sqlite3/lib/binding/node-v48-darwin-x64/node_sqlite3.node&quot; is installed via remote
&#10;&gt; @mapbox/mapbox-gl-native@3.5.4 install /usr/local/lib/node_modules/tileserver-gl/node_modules/@mapbox/mapbox-gl-native
&gt; node-pre-gyp install --fallback-to-build=false || make node
&#10;[@mapbox/mapbox-gl-native] Success: &quot;/usr/local/lib/node_modules/tileserver-gl/node_modules/@mapbox/mapbox-gl-native/lib/mapbox_gl_native.node&quot; is installed via remote
&#10;&gt; canvas@1.6.8 install /usr/local/lib/node_modules/tileserver-gl/node_modules/canvas
&gt; node-gyp rebuild
&#10;gyp WARN EACCES user &quot;root&quot; does not have permission to access the dev dir &quot;/Users/rajavelu-1469/.node-gyp/6.11.3&quot;
gyp WARN EACCES attempting to reinstall using temporary dev dir &quot;/usr/local/lib/node_modules/tileserver-gl/node_modules/canvas/.node-gyp&quot;
./util/has_lib.sh: line 31: pkg-config: command not found
gyp: Call to &#39;./util/has_lib.sh freetype&#39; returned exit status 0 while in binding.gyp. while trying to load binding.gyp
gyp ERR! configure error 
gyp ERR! stack Error: `gyp` failed with exit code: 1
gyp ERR! stack     at ChildProcess.onCpExit (/usr/local/lib/node_modules/npm/node_modules/node-gyp/lib/configure.js:305:16)
gyp ERR! stack     at emitTwo (events.js:106:13)
gyp ERR! stack     at ChildProcess.emit (events.js:191:7)
gyp ERR! stack     at Process.ChildProcess._handle.onexit (internal/child_process.js:219:12)
gyp ERR! System Darwin 16.7.0
gyp ERR! command &quot;/usr/local/bin/node&quot; &quot;/usr/local/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js&quot; &quot;rebuild&quot;
gyp ERR! cwd /usr/local/lib/node_modules/tileserver-gl/node_modules/canvas
gyp ERR! node -v v6.11.3
gyp ERR! node-gyp -v v3.4.0
gyp ERR! not ok 
/usr/local/lib
└── (empty)
&#10;npm ERR! Darwin 16.7.0
npm ERR! argv &quot;/usr/local/bin/node&quot; &quot;/usr/local/bin/npm&quot; &quot;install&quot; &quot;-g&quot; &quot;tileserver-gl&quot;
npm ERR! node v6.11.3
npm ERR! npm  v3.10.10
npm ERR! code ELIFECYCLE
&#10;npm ERR! canvas@1.6.8 install: `node-gyp rebuild`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the canvas@1.6.8 install script &#39;node-gyp rebuild&#39;.
npm ERR! Make sure you have the latest version of node.js and npm installed.
npm ERR! If you do, this is most likely a problem with the canvas package,
npm ERR! not with npm itself.
npm ERR! Tell the author that this fails on your system:
npm ERR!     node-gyp rebuild
npm ERR! You can get information on how to open an issue for this project with:
npm ERR!     npm bugs canvas
npm ERR! Or if that isn&#39;t available, you can get their info via:
npm ERR!     npm owner ls canvas
npm ERR! There is likely additional logging output above.
&#10;npm ERR! Please include the following file with any support request:
npm ERR!     /Users/rajavelu-1469/npm-debug.log
npm ERR! code 1</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-staticmap" rel="tag" title="see questions tagged &#39;staticmap&#39;">staticmap</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '18, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Mar '18, 08:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-62520" class="comments-container">
<span id="62573"></span>
<div id="comment-62573" class="comment">
<div id="post-62573-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also tried in centos machine &amp; got following error, any idea?</p>
<blockquote>
<p>tileserver-gl</p>
</blockquote>
<p>Starting tileserver-gl v2.3.1</p>
<p>No MBTiles specified, using india.mbtiles</p>
<p>Automatically creating config file for india.mbtiles</p>
<p>Run with --verbose to see the config file here.</p>
<p>module.js:471</p>
<pre><code>throw err;
^</code></pre>
<p>Error: Cannot find module '../build/Release/sharp.node'</p>
<pre><code>at Function.Module._resolveFilename (module.js:469:15)
&#10;at Function.Module._load (module.js:417:25)
&#10;at Module.require (module.js:497:17)
&#10;at require (internal/module.js:20:19)
&#10;at Object.&lt;anonymous&gt; (/usr/lib/node_modules/tileserver-gl/node_modules/sharp/lib/constructor.js:9:15)
&#10;at Module._compile (module.js:570:32)
&#10;at Object.Module._extensions..js (module.js:579:10)
&#10;at Module.load (module.js:487:32)
&#10;at tryModuleLoad (module.js:446:12)
&#10;at Function.Module._load (module.js:438:3)</code></pre>
</div>
<div id="comment-62573-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 10:47)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-62520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62520-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


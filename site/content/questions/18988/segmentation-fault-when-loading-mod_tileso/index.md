+++
type = "question"
title = "segmentation fault when loading mod_tile.so"
description = '''After following Ubuntu tile server setup instructions I encounter the following segmentation fault any time Apache2 is started. I&#x27;ve attempted re-installing mod_tile from SVN but still hit this crash. user@host:~$ sudo /etc/init.d/apache2 start  * Starting web server apache2 [Fri Jan 11 13:25:59 201...'''
date = "2013-01-11T21:33:00Z"
lastmod = "2013-01-12T16:11:00Z"
weight = 18988
keywords = [ "segmentation", "mod_tile", "apache2" ]
aliases = [ "/questions/18988" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [segmentation fault when loading mod_tile.so](/questions/18988/segmentation-fault-when-loading-mod_tileso)

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
<span id="post-18988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After following <a href="http://wiki.openstreetmap.org/wiki/Ubuntu_tile_server" title="Ubuntu tile server setup instructions">Ubuntu tile server setup instructions</a> I encounter the following segmentation fault any time Apache2 is started. I've attempted <a href="http://wiki.openstreetmap.org/wiki/Mod_tile#Install_mod_tile_From_Source" title="Install mod_tile from source">re-installing mod_tile from SVN</a> but still hit this crash.</p>
<pre><code>user@host:~$ sudo /etc/init.d/apache2 start
 * Starting web server apache2                                                                                                                                                                                                                                                                                                [Fri Jan 11 13:25:59 2013] [notice] Committing tile config default
[Fri Jan 11 13:25:59 2013] [notice] Loading tile config default at /osm/ for zooms 0 - 18 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
*** glibc detected *** /usr/sbin/apache2: double free or corruption (fasttop): 0x00007fa6fc5859f0 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x7eb96)[0x7fa6fa7f9b96]
/usr/lib/apache2/modules/mod_tile.so(+0xaa00)[0x7fa6f7847a00]
/usr/sbin/apache2(+0x417d1)[0x7fa6fb6567d1]
/usr/sbin/apache2(ap_walk_config+0xb7)[0x7fa6fb658807]
/usr/sbin/apache2(+0x3b20a)[0x7fa6fb65020a]
/usr/sbin/apache2(+0x417ee)[0x7fa6fb6567ee]
/usr/sbin/apache2(ap_walk_config+0xb7)[0x7fa6fb658807]
/usr/sbin/apache2(ap_process_config_tree+0xd2)[0x7fa6fb659722]
/usr/sbin/apache2(main+0x98d)[0x7fa6fb641f5d]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xed)[0x7fa6fa79c76d]
/usr/sbin/apache2(+0x2d2a9)[0x7fa6fb6422a9]
======= Memory map: ========
.... omitted ....</code></pre>
<p>So I grabbed a core dump and did some mucking around in gdb at frame 4 we see load_tile_config() get called then everything falls to pieces. Appears to be a double free in mod_tile.c in load_tile_config(), a quick look through the function didn't turn up anything that should cause the crash but I don't know this code base so maybe I missed something :/</p>
<pre><code>#0  0x00007f5e09a65425 in __GI_raise (sig=&lt;optimized out&gt;) at ../nptl/sysdeps/unix/sysv/linux/raise.c:64
#1  0x00007f5e09a68b8b in __GI_abort () at abort.c:91
#2  0x00007f5e09aa339e in __libc_message (do_abort=2, fmt=0x7f5e09bad028 &quot;*** glibc detected *** %s: %s: 0x%s ***\n&quot;) at ../sysdeps/unix/sysv/linux/libc_fatal.c:201
#3  0x00007f5e09aadb96 in malloc_printerr (action=3, str=0x7f5e09bad218 &quot;double free or corruption (fasttop)&quot;, ptr=&lt;optimized out&gt;) at malloc.c:5007
#4  0x00007f5e06afba00 in load_tile_config () from /usr/lib/apache2/modules/mod_tile.so
#5  0x00007f5e0a90a7d1 in invoke_cmd (cmd=0x7f5e06cff9c0 &lt;tile_cmds&gt;, parms=parms@entry=0x7fffa0cb77e0, mconfig=0x0, args=0x7f5e06a7c369 &quot;&quot;) at config.c:791
#6  0x00007f5e0a90c807 in ap_walk_config_sub (section_vector=0x7f5e0a82fea8, parms=0x7fffa0cb77e0, current=0x7f5e06a7c318) at config.c:1164
#7  ap_walk_config (current=0x7f5e06a7c318, parms=parms@entry=0x7fffa0cb77e0, section_vector=0x7f5e0a82fea8) at config.c:1197
#8  0x00007f5e0a90420a in virtualhost_section (cmd=0x7fffa0cb77e0, dummy=&lt;optimized out&gt;, arg=&lt;optimized out&gt;) at core.c:2234
#9  0x00007f5e0a90a7ee in invoke_cmd (cmd=0x7f5e0ab365d0 &lt;core_cmds+80&gt;, parms=parms@entry=0x7fffa0cb77e0, mconfig=0x7f5e0a87e318, args=0x7f5e06a7c0d8 &quot;*:80&gt;&quot;) at config.c:758
#10 0x00007f5e0a90c807 in ap_walk_config_sub (section_vector=0x7f5e0a87dee0, parms=0x7fffa0cb77e0, current=0x7f5e06a7c098) at config.c:1164
#11 ap_walk_config (current=0x7f5e06a7c098, parms=parms@entry=0x7fffa0cb77e0, section_vector=0x7f5e0a87dee0) at config.c:1197
#12 0x00007f5e0a90d722 in ap_process_config_tree (s=s@entry=0x7f5e0a8b5578, conftree=&lt;optimized out&gt;, p=0x7f5e0a8bc028, ptemp=&lt;optimized out&gt;) at config.c:1792
#13 0x00007f5e0a8f5f5d in main (argc=3, argv=0x7fffa0cb7a38) at main.c:647</code></pre>
<p>Any help/advice?</p>
<p><strong>Config files</strong></p>
<p><a href="http://www.nullagent.com/public/scratch/renderd.conf">/etc/renderd.conf</a></p>
<p><a href="http://www.nullagent.com/public/scratch/apache2.conf">/etc/apache2/apache2.conf</a></p>
<p><a href="http://www.nullagent.com/public/scratch/tile.load">/etc/apache2/mods-available/tile.load</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segmentation" rel="tag" title="see questions tagged &#39;segmentation&#39;">segmentation</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-apache2" rel="tag" title="see questions tagged &#39;apache2&#39;">apache2</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '13, 21:33</strong></p>
<img src="https://secure.gravatar.com/avatar/b3ef7c0ff8d75d77bd61b27a24f3e446?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="7bitbyte&#39;s gravatar image" />
<p><span>7bitbyte</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="7bitbyte has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '13, 22:45</strong> </span></p>
</div>
</div>
<div id="comments-container-18988" class="comments-container">
<span id="18989"></span>
<div id="comment-18989" class="comment not_top_scorer">
<div id="post-18989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What version of Unbuntu is this with?</p>
</div>
<div id="comment-18989-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 21:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18990"></span>
<div id="comment-18990" class="comment not_top_scorer">
<div id="post-18990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ubuntu 12.10 quantal running on a 64bit machine</p>
</div>
<div id="comment-18990-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 22:05)</span> <span class="comment-user userinfo">7bitbyte</span>
</div>
</div>
<span id="18991"></span>
<div id="comment-18991" class="comment">
<div id="post-18991-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I was hitting this on 12.04, preformed the update to 12.10 and still hit so I started digging deeper.</p>
</div>
<div id="comment-18991-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 22:07)</span> <span class="comment-user userinfo">7bitbyte</span>
</div>
</div>
<span id="18992"></span>
<div id="comment-18992" class="comment">
<div id="post-18992-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Although I haven't tested the 12.10 version yet, so it is possible that there is a general bug, I rather suspect there is something in the config that upsets it (of cause that is also a bug, but perhaps easier to work around). Could you post the site config and the renderd config?</p>
</div>
<div id="comment-18992-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 22:27)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="18993"></span>
<div id="comment-18993" class="comment not_top_scorer">
<div id="post-18993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point, updated post to include links to config files</p>
</div>
<div id="comment-18993-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 22:46)</span> <span class="comment-user userinfo">7bitbyte</span>
</div>
</div>
<span id="18994"></span>
<div id="comment-18994" class="comment">
<div id="post-18994-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can avoid the crash now by removing the ATTRIBUTION and DESCRIPTION tags from /etc/renderd.conf but there is definitely a bug in mod_tile</p>
</div>
<div id="comment-18994-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 23:02)</span> <span class="comment-user userinfo">7bitbyte</span>
</div>
</div>
<span id="18995"></span>
<div id="comment-18995" class="comment">
<div id="post-18995-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>hey, i have the same error.</p>
<p>i didnt tested it yet, but have a look at the end of the method load_tile_config()</p>
<p>if (description) free(description);</p>
<p>if (attribution) free(description);</p>
<p>if (hostnames) free(description);</p>
<p>that looks wrong :)</p>
<p>edit: that fixed it for me</p>
<p>if (description) free(description);</p>
<p>if (attribution) free(attribution);</p>
<p>if (hostnames) free(hostnames);</p>
</div>
<div id="comment-18995-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 23:20)</span> <span class="comment-user userinfo">fabianpr</span>
</div>
</div>
<span id="18996"></span>
<div id="comment-18996" class="comment not_top_scorer">
<div id="post-18996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>doh, yep that should be the issue.</p>
</div>
<div id="comment-18996-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 23:41)</span> <span class="comment-user userinfo">7bitbyte</span>
</div>
</div>
<span id="18997"></span>
<div id="comment-18997" class="comment">
<div id="post-18997-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ah, yes, that is indeed wrong. I'll commit a fix for that soon. I wonder if I committed the wrong version, as I noticed that error before committing and thought I had already fixed it. Oh well... Thanks for the report.</p>
</div>
<div id="comment-18997-info" class="comment-info">
<span class="comment-age">(12 Jan '13, 00:47)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="19006"></span>
<div id="comment-19006" class="comment not_top_scorer">
<div id="post-19006-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I fixed those double frees in SVN revision 29190 now. Hopefully that will solve the issue. Could you please confirm this? I will also upload a fixed package soon.</p>
</div>
<div id="comment-19006-info" class="comment-info">
<span class="comment-age">(12 Jan '13, 16:11)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-18988" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-18988-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


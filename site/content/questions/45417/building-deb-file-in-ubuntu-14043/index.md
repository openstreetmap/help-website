+++
type = "question"
title = "Building deb file in Ubuntu 14.04.3"
description = '''So I encountered a bug and the solution is to download the latest sources and build. But as I have quite a number of hosts, I want to make a deb file. But it fails with the error below. I can&#x27;t really figure out what the error is. I do the following: sudo apt-get install make g++ Automake qt4-defaul...'''
date = "2015-08-27T13:11:00Z"
lastmod = "2015-08-27T13:11:00Z"
weight = 45417
keywords = [ "build_error" ]
aliases = [ "/questions/45417" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Building deb file in Ubuntu 14.04.3](/questions/45417/building-deb-file-in-ubuntu-14043)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45417-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I encountered a bug and the solution is to download the latest sources and build. But as I have quite a number of hosts, I want to make a deb file. But it fails with the error below. I can't really figure out what the error is.</p><p>I do the following:</p><pre><code>sudo apt-get install make g++ Automake qt4-default fakeroot docbook-xml quilt libnl-genl-3-dev libnl-route-3-dev asciidoc cmake
cd /tmp # do not use NFS
wget --no-check-certificate https://1.as.dl.wireshark.org/src/wireshark-1.12.7.tar.bz2
tar -xf wireshark-1.12.7.tar.bz2
cd wireshark-1.12.7
./configure
make debian-package</code></pre><p>After some time I get this error:</p><pre><code>- Enabled features:

-- Disabled features:

-- Docdir install: /usr/share/doc/wireshark-doc
-- Configuring incomplete, errors occurred!
See also &quot;/tmp/wireshark-1.12.7/obj-x86_64-linux-gnu/CMakeFiles/CMakeOutput.log&quot;.
See also &quot;/tmp/wireshark-1.12.7/obj-x86_64-linux-gnu/CMakeFiles/CMakeError.log&quot;.
dh_auto_configure: cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_BUILD_TYPE=None -DENABLE_GUIDES=ON -DCMAKE_INSTALL_LIBDIR=/usr/lib/x86_64-linux-gnu -DENABLE_QT5=OFF returned exit code 1
make[2]: *** [override_dh_auto_configure] Error 2
make[2]: Leaving directory `/tmp/wireshark-1.12.7&#39;
make[1]: *** [build] Error 2
make[1]: Leaving directory `/tmp/wireshark-1.12.7&#39;
dpkg-buildpackage: error: debian/rules build gave error exit status 2
make: *** [debian-package] Error 2</code></pre><p>My version</p><pre><code>$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.3 LTS
Release:    14.04
Codename:   trusty</code></pre></div><div id="question-tags" class="tags-container tags">build_error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '15, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/b0ac00407121781dba912c3cd3ede4c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kjeld%20Flarup&#39;s gravatar image" /><p>Kjeld Flarup<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kjeld Flarup has no accepted answers">0%</span></p></div></div><div id="comments-container-45417" class="comments-container"></div><div id="comment-tools-45417" class="comment-tools"></div><div class="clear"></div><div id="comment-45417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


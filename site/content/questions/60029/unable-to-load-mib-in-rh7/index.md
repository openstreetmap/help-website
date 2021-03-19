+++
type = "question"
title = "Unable to load MIB in RH7"
description = '''Hi, Im trying to load a MIB in tshark for parsing some OIDs to text values. I&#x27;ve read that I need to modify the files: /.wireshark/preferences /.wireshark/smipaths ~/.wireshark/smimodules but the problem is that I cannot find those files in my machine. The wireshark was installed as root and I canno...'''
date = "2017-03-13T06:08:00Z"
lastmod = "2017-03-14T00:11:00Z"
weight = 60029
keywords = [ "mib", "snmp" ]
aliases = [ "/questions/60029" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to load MIB in RH7](/questions/60029/unable-to-load-mib-in-rh7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60029-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Im trying to load a MIB in tshark for parsing some OIDs to text values. I've read that I need to modify the files:</p><p>/.wireshark/preferences /.wireshark/smipaths ~/.wireshark/smimodules</p><p>but the problem is that I cannot find those files in my machine. The wireshark was installed as root and I cannot find this ".wireshark" folder. Inside the wireshark directory (/usr/share/wireshark) I have only the following files:</p><p>AUTHORS-SHORT COPYING dtds ipmap.html radius smi_modules wimaxasncp capinfos.html dfilters dumpcap.html manuf randpkt.html text2pcap.html wireshark-filter.html cfilters dftest.html editcap.html mergecap.html rawshark.html tpncp wireshark.html colorfilters diameter help pdml2html.xsl services tshark.html ws.css</p><p>I'm using a Red Hat Enterprise Linux Server release 6.5.</p></div><div id="question-tags" class="tags-container tags">mib snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '17, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/de7a9d9ed45afd16777c43053086fdf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psh1982&#39;s gravatar image" /><p>psh1982<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psh1982 has no accepted answers">0%</span></p></div></div><div id="comments-container-60029" class="comments-container"></div><div id="comment-tools-60029" class="comment-tools"></div><div class="clear"></div><div id="comment-60029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60041"></span>

<div id="answer-container-60041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60041-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This <code>.wireshark</code> directory should be available in your home directory. What your home directory is depends on the account you use to run Wireshark. Your normal user account should be based in <code>/home</code>, but if you run it as the root user it should be found in <code>/root</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '17, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60041" class="comments-container"><span id="60083"></span><div id="comment-60083" class="comment"><div id="post-60083-score" class="comment-score"></div><div class="comment-text"><p>I appreciate your reply, but I cannot find the wireshark directory in /root:</p><p>[[email protected] ~]# pwd /root [[email protected] ~]# cd .wireshark bash: cd: .wireshark: No such file or directory [[email protected] ~]# find / -name .wireshark [[email protected] ~]#</p></div><div id="comment-60083-info" class="comment-info"><span class="comment-age">(15 Mar '17, 02:48)</span> psh1982</div></div></div><div id="comment-tools-60041" class="comment-tools"></div><div class="clear"></div><div id="comment-60041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60048"></span>

<div id="answer-container-60048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60048-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To get the directories used by tshark you can run <code>tshark -G folders</code>.</p><p>The values of <code>Personal configuration</code> and <code>Global configuration</code> lists the directory where your files should be located.</p><p>For SNMP decoding you have to use the preference <code>nameres.load_smi_modules: TRUE</code> (in the <code>preferences</code> file or using the <code>-o</code> option).</p><p>To specify the folder(s) where your MIB files are located use the file <code>smi_paths</code>.</p><p>To specify the MIBs to load use the file <code>smi_modules</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '17, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '17, 00:16</p></div></div><div id="comments-container-60048" class="comments-container"><span id="60081"></span><div id="comment-60081" class="comment"><div id="post-60081-score" class="comment-score"></div><div class="comment-text"><p>I don´t have the "tshark -G folders" enabled:</p><pre><code> [[email protected] sysadmin]# tshark -G folders
    tshark: Invalid &quot;folders&quot; option for -G flag, enter -G ? for more help.
    [[email protected] sysadmin]# tshark -G ?
    TShark 1.8.10 (SVN Rev Unknown from unknown)

    Usage: tshark -G [report]

    Glossary table reports:
      -G [fields]              dump glossary in original format and exit
      -G fields2               dump glossary in format 2 and exit
      -G fields3               dump glossary in format 3 and exit
      -G protocols             dump protocols in registration database and exit
      -G values                dump value, range, true/false strings and exit
      -G ftypes                dump field type basic and descriptive names
      -G decodes               dump &quot;layer type&quot;/&quot;decode as&quot; associations and exit
      -G heuristic-decodes     dump heuristic dissector tables

    Preference reports:
      -G defaultprefs          dump default preferences and exit
      -G currentprefs          dump current preferences and exit</code></pre><p>I cannot find also the .wireshark directory in /root:</p><pre><code>[[email protected] ~]# pwd
/root 
[[email protected] ~]# cd .wireshark
bash: cd: .wireshark: No such file or directory
[[email protected] ~]# find / -name .wireshark
[[email protected] ~]#</code></pre></div><div id="comment-60081-info" class="comment-info"><span class="comment-age">(15 Mar '17, 02:44)</span> psh1982</div></div><span id="60086"></span><div id="comment-60086" class="comment"><div id="post-60086-score" class="comment-score"></div><div class="comment-text"><p>Ah, I'm sorry. The <code>tshark -G folders</code> option is only available in the current master branch (2.3.X).</p><p>The personal configuration should be in $HOME/.wireshark. If this directory is missing you have to create it <code>mkdir $HOME/.wireshark/</code></p></div><div id="comment-60086-info" class="comment-info"><span class="comment-age">(15 Mar '17, 04:58)</span> Uli</div></div><span id="60090"></span><div id="comment-60090" class="comment"><div id="post-60090-score" class="comment-score"></div><div class="comment-text"><p>thanks for answering again :)</p><p>I've created the files but I get a warning:</p><pre><code>[[email protected] .wireshark]# sudo tshark -i any -d udp.port==9000,snmp -f &quot;port 9000&quot; -O snmp -R snmp.value.octets==38:38:2d:37:33:2d:38:34:2d:35:33:2d:30:30:2d:30:30:2d:30:38:2d:46:32 -c 1 | egrep &quot;Object Name|Value&quot;

** (process:2955): WARNING **: /root/.wireshark/preferences line 1: No such preference &quot;nameres.load_smi_modules&quot; (applying your preferences once should remove this warning)</code></pre><p>The directory and files created:</p><pre><code>[[email protected] .wireshark]# ls -l
total 12
-rw-r--r-- 1 root root 31 Mar 15 16:57 preferences
-rw-r--r-- 1 root root 17 Mar 15 17:10 smi_modules
-rw-r--r-- 1 root root 22 Mar 15 17:11 smi_paths
[[email protected] .wireshark]# cat preferences
nameres.load_smi_modules: TRUE
[[email protected] .wireshark]# cat smi_modules
&quot;SMIP-TRAPS-MIB&quot;
[[email protected] .wireshark]# cat smi_paths
/usr/share/snmp/mibs/</code></pre></div><div id="comment-60090-info" class="comment-info"><span class="comment-age">(15 Mar '17, 09:22)</span> psh1982</div></div><span id="60097"></span><div id="comment-60097" class="comment"><div id="post-60097-score" class="comment-score"></div><div class="comment-text"><p>Just saw you're using an old, unsupported version (1.8.10). If I remember right option was <code>prefs.load_smi_modules</code> with this version.</p></div><div id="comment-60097-info" class="comment-info"><span class="comment-age">(15 Mar '17, 12:32)</span> Uli</div></div><span id="60103"></span><div id="comment-60103" class="comment"><div id="post-60103-score" class="comment-score"></div><div class="comment-text"><p>Just looked at the code from back then, I think it was "name_resolve_load_smi_modules"</p></div><div id="comment-60103-info" class="comment-info"><span class="comment-age">(15 Mar '17, 16:38)</span> Jaap ♦</div></div></div><div id="comment-tools-60048" class="comment-tools"></div><div class="clear"></div><div id="comment-60048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


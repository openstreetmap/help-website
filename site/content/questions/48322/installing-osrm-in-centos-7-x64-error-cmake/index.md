+++
type = "question"
title = "Installing OSRM in CENTOS 7 x64 - error Cmake .."
description = '''I&#x27;m trying to install osrm in my server centos 7, but i can&#x27;t do it... i tried a lot and differents ways.. but i can&#x27;t  [root@u18343387 build]# cmake .. -- Building on a 64 bit system -- Configuring OSRM in release mode -- Setting linker optimizations -- Boost version: 1.52.0 -- Found the following ...'''
date = "2016-02-24T07:24:00Z"
lastmod = "2016-02-25T15:36:00Z"
weight = 48322
keywords = [ "osrm", "problem", "cmake", "installation", "centos" ]
aliases = [ "/questions/48322" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Installing OSRM in CENTOS 7 x64 - error Cmake ..](/questions/48322/installing-osrm-in-centos-7-x64-error-cmake)

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
<span id="post-48322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>I'm trying to install osrm in my server centos 7, but i can't do it... i tried a lot and differents ways.. but i can't</strong></p>
<hr />
<pre><code>[root@u18343387 build]# cmake ..
-- Building on a 64 bit system
-- Configuring OSRM in release mode
-- Setting linker optimizations
-- Boost version: 1.52.0
-- Found the following Boost libraries:
--   date_time
--   filesystem
--   iostreams
--   program_options
--   regex
--   system
--   thread
--   unit_test_framework
-- Found Intel TBB
-- Looking for Luabind...
CMake Error at /usr/local/share/cmake-3.4/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find Luabind (missing: LUABIND_LIBRARIES LUABIND_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/share/cmake-3.4/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindLuabind.cmake:64 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
  CMakeLists.txt:247 (find_package)</code></pre>
<hr />
<p><strong>what can i do... plx, explane me, i'm a new in this... this the content of the file cmake error</strong></p>
<hr />
<pre><code>Performing C++ SOURCE FILE Test LTO_AVAILABLE failed with the following output:
Change Dir: /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp
&#10;Run Build Command:/usr/bin/gmake &quot;cmTryCompileExec2838510061/fast&quot;
/usr/bin/gmake -f CMakeFiles/cmTryCompileExec2838510061.dir/build.make CMakeFiles/cmTryCompileExec2838510061.dir/build
gmake[1]: Entering directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
/usr/bin/cmake -E cmake_progress_report /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/CMakeFiles 1
Building CXX object CMakeFiles/cmTryCompileExec2838510061.dir/src.cxx.o
/usr/bin/c++    -DLTO_AVAILABLE   -flto -o CMakeFiles/cmTryCompileExec2838510061.dir/src.cxx.o -c /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/src.cxx
cc1plus: error: unrecognized command line option &quot;-flto&quot;
gmake[1]: *** [CMakeFiles/cmTryCompileExec2838510061.dir/src.cxx.o] Error 1
gmake[1]: Leaving directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
gmake: *** [cmTryCompileExec2838510061/fast] Error 2
&#10;Source file was:
int main() { return 0;}
Performing C++ SOURCE FILE Test HAS_COLOR_FLAG failed with the following output:
Change Dir: /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp
&#10;Run Build Command:/usr/bin/gmake &quot;cmTryCompileExec2322203982/fast&quot;
/usr/bin/gmake -f CMakeFiles/cmTryCompileExec2322203982.dir/build.make CMakeFiles/cmTryCompileExec2322203982.dir/build
gmake[1]: Entering directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
/usr/bin/cmake -E cmake_progress_report /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/CMakeFiles 1
Building CXX object CMakeFiles/cmTryCompileExec2322203982.dir/src.cxx.o
/usr/bin/c++    -DHAS_COLOR_FLAG   -fdiagnostics-color=auto -o CMakeFiles/cmTryCompileExec2322203982.dir/src.cxx.o -c /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/src.cxx
cc1plus: error: unrecognized command line option &quot;-fdiagnostics-color=auto&quot;
gmake[1]: *** [CMakeFiles/cmTryCompileExec2322203982.dir/src.cxx.o] Error 1
gmake[1]: Leaving directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
gmake: *** [cmTryCompileExec2322203982/fast] Error 2
&#10;Source file was:
int main() { return 0;}
Determining if the pthread_create exist failed with the following output:
Change Dir: /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp
&#10;Run Build Command:/usr/bin/gmake &quot;cmTryCompileExec869518868/fast&quot;
/usr/bin/gmake -f CMakeFiles/cmTryCompileExec869518868.dir/build.make CMakeFiles/cmTryCompileExec869518868.dir/build
gmake[1]: Entering directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
/usr/bin/cmake -E cmake_progress_report /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/CMakeFiles 1
Building C object CMakeFiles/cmTryCompileExec869518868.dir/CheckSymbolExists.c.o
/usr/bin/cc    -o CMakeFiles/cmTryCompileExec869518868.dir/CheckSymbolExists.c.o   -c /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/CheckSymbolExists.c
Linking C executable cmTryCompileExec869518868
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTryCompileExec869518868.dir/link.txt --verbose=1
/usr/bin/cc       CMakeFiles/cmTryCompileExec869518868.dir/CheckSymbolExists.c.o  -o cmTryCompileExec869518868 -rdynamic 
CMakeFiles/cmTryCompileExec869518868.dir/CheckSymbolExists.c.o: In function `main&#39;:
CheckSymbolExists.c:(.text+0xc): undefined reference to `pthread_create&#39;
collect2: ld returned 1 exit status
gmake[1]: *** [cmTryCompileExec869518868] Error 1
gmake[1]: Leaving directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
gmake: *** [cmTryCompileExec869518868/fast] Error 2
&#10;File /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/CheckSymbolExists.c:
/* */
#include &lt;pthread.h&gt;
&#10;int main(int argc, char** argv)
{
  (void)argv;
#ifndef pthread_create
  return ((int*)(&amp;pthread_create))[argc];
#else
  (void)argc;
  return 0;
#endif
}
&#10;Determining if the function pthread_create exists in the pthreads failed with the following output:
Change Dir: /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp
&#10;Run Build Command:/usr/bin/gmake &quot;cmTryCompileExec1634399928/fast&quot;
/usr/bin/gmake -f CMakeFiles/cmTryCompileExec1634399928.dir/build.make CMakeFiles/cmTryCompileExec1634399928.dir/build
gmake[1]: Entering directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
/usr/bin/cmake -E cmake_progress_report /home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp/CMakeFiles 1
Building C object CMakeFiles/cmTryCompileExec1634399928.dir/CheckFunctionExists.c.o
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=pthread_create   -o CMakeFiles/cmTryCompileExec1634399928.dir/CheckFunctionExists.c.o   -c /usr/share/cmake/Modules/CheckFunctionExists.c
Linking C executable cmTryCompileExec1634399928
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTryCompileExec1634399928.dir/link.txt --verbose=1
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=pthread_create    CMakeFiles/cmTryCompileExec1634399928.dir/CheckFunctionExists.c.o  -o cmTryCompileExec1634399928 -rdynamic -lpthreads 
/usr/bin/ld: cannot find -lpthreads
collect2: ld returned 1 exit status
gmake[1]: *** [cmTryCompileExec1634399928] Error 1
gmake[1]: Leaving directory `/home/osrm/osrm-backend/build/CMakeFiles/CMakeTmp&#39;
gmake: *** [cmTryCompileExec1634399928/fast] Error 2</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-cmake" rel="tag" title="see questions tagged &#39;cmake&#39;">cmake</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '16, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/9bd2a84fbfcb6ee54b372f83189bb6d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarckBlezzer&#39;s gravatar image" />
<p><span>DarckBlezzer</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarckBlezzer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '16, 07:28</strong> </span></p>
</div>
</div>
<div id="comments-container-48322" class="comments-container">
&#10;</div>
<div id="comment-tools-48322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48322-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="48323"></span>

<div id="answer-container-48323" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>Make Error at /usr/local/share/cmake-3.4/Modules/FindPackageHandleStandardArgs.cmake:148 (message):   Could NOT find Luabind (missing: LUABIND_LIBRARIES LUABIND_INCLUDE_DIR)</code></pre>
<p>You have to install luabind. See <a href="https://github.com/Project-OSRM/osrm-backend/wiki/Building-OSRM">Building OSRM</a> in the OSRM wiki for information on how to build OSRM on CentOS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '16, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48323" class="comments-container">
<span id="48335"></span>
<div id="comment-48335" class="comment">
<div id="post-48335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i have this error</p>
<pre><code>-- Building on a 64 bit system
-- Configuring OSRM in release mode
-- Setting linker optimizations
-- Boost version: 1.52.0
-- Found the following Boost libraries:
--   date_time
--   filesystem
--   iostreams
--   program_options
--   regex
--   system
--   thread
--   unit_test_framework
-- Found Intel TBB
-- Looking for Luabind...
-- Found Luabind: /opt/osrm_infrastructure/luabind-0.9.1/lib/libluabindd.so
-- Found Luabind: /opt/osrm_infrastructure/luabind-0.9.1/lib/libluabindd.so
-- Found Lua52: /usr/lib64/liblua.so;/usr/lib64/libm.so (found version &quot;5.1.4&quot;)
-- Looking for LuaJIT 5.2
-- Found LUAJIT: /opt/osrm_infrastructure/LuaJIT-2.0.2/lib/libluajit-5.1.so
-- Found LuaJIT: LUAJIT_LIBRARY-NOTFOUND
-- Performing Test LUABIND_WORKS
-- Performing Test LUABIND_WORKS - Failed
-- Luabind/Lua5.2 not feasible, falling back to Lua 5.1.
-- Found Lua51: /usr/lib64/liblua.so;/usr/lib64/libm.so (found version &quot;5.1.4&quot;)
-- Looking for LuaJIT 5.1
-- Found LuaJIT: LUAJIT_LIBRARY-NOTFOUND
-- Performing Test LUABIND51_WORKS
-- Performing Test LUABIND51_WORKS - Failed
CMake Error at cmake/check_luabind.cmake:38 (message):
  Luabind does not work with Lua 5.1 at /usr/lib64/liblua-5.1.so, no working
  Luabind found
Call Stack (most recent call first</code></pre>
<p>I need to downgrade lua???</p>
</div>
<div id="comment-48335-info" class="comment-info">
<span class="comment-age">(24 Feb '16, 16:34)</span> <span class="comment-user userinfo">DarckBlezzer</span>
</div>
</div>
<span id="48336"></span>
<div id="comment-48336" class="comment">
<div id="post-48336-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The first hit when searching for "Luabind does not work with Lua 5.1" is <a href="https://github.com/Project-OSRM/osrm-backend/issues/1196">OSRM issue 1196</a>. According to the comments this can happen if you have a parallel installation of lua 5.1 and 5.2 (which should be fixed if I understood correctly) or your system has not enough memory. The latter is also explained in <a href="https://github.com/Project-OSRM/osrm-backend/issues/1580">issue 1580</a>.</p>
</div>
<div id="comment-48336-info" class="comment-info">
<span class="comment-age">(24 Feb '16, 17:22)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48323-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48343"></span>

<div id="answer-container-48343" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48343-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well i have less error, but i can't pass from this, i don't know how to downgrade or change the LUA,</p>
<p>now i have this error</p>
<pre><code>[root@u18343387 build]# cmake ..
-- Building on a 64 bit system
-- Configuring OSRM in release mode
-- Setting linker optimizations
-- Boost version: 1.52.0
-- Found the following Boost libraries:
--   date_time
--   filesystem
--   iostreams
--   program_options
--   regex
--   system
--   thread
--   unit_test_framework
-- Found Intel TBB
-- Looking for Luabind...
-- Found Luabind: /opt/osrm_infrastructure/luabind-0.9.1/lib/libluabindd.so
-- Looking for LuaJIT 5.2
-- Found LuaJIT: LUAJIT_LIBRARY-NOTFOUND
-- Performing Test LUABIND_WORKS
-- Performing Test LUABIND_WORKS - Failed
-- Luabind/Lua5.2 not feasible, falling back to Lua 5.1.
-- Found Lua51: /usr/lib64/liblua.so;/usr/lib64/libm.so
-- Looking for LuaJIT 5.1
-- Found LuaJIT: LUAJIT_LIBRARY-NOTFOUND
-- Performing Test LUABIND51_WORKS
-- Performing Test LUABIND51_WORKS - Failed
CMake Error at cmake/check_luabind.cmake:38 (message):
  Luabind does not work with Lua 5.1 at /usr/lib64/liblua-5.1.so, no working
  Luabind found
Call Stack (most recent call first):
  CMakeLists.txt:248 (include)
&#10;
-- Configuring incomplete, errors occurred!
See also &quot;/home/osrm/osrm-backend/build/CMakeFiles/CMakeOutput.log&quot;.
See also &quot;/home/osrm/osrm-backend/build/CMakeFiles/CMakeError.log&quot;.</code></pre>
<p>i saw the last links but i can't find a answer to change or somthing to make it run correctly</p>
<pre><code>[root@u18343387 build]# rpm -qa | grep lua
lua-devel-5.1.4-4.1.el6.x86_64
lua-5.1.4-4.1.el6.x86_64</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '16, 23:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9bd2a84fbfcb6ee54b372f83189bb6d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarckBlezzer&#39;s gravatar image" />
<p><span>DarckBlezzer</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarckBlezzer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '16, 23:26</strong> </span></p>
</div>
</div>
<div id="comments-container-48343" class="comments-container">
<span id="48344"></span>
<div id="comment-48344" class="comment">
<div id="post-48344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you check for the other cause of the problem I mentioned in my comment, i.e. too few memory?</p>
</div>
<div id="comment-48344-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 08:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48357"></span>
<div id="comment-48357" class="comment">
<div id="post-48357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the server has 16 gb of ram, and i think it doesn't affect,or not?</p>
</div>
<div id="comment-48357-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 15:36)</span> <span class="comment-user userinfo">DarckBlezzer</span>
</div>
</div>
</div>
<div id="comment-tools-48343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48343-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

